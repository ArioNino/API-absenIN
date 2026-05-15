import logging
from datetime import datetime
from typing import List, Literal, Optional

from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile, status
from sqlalchemy.orm import Session

from app.config import get_settings
from app.database import get_db
from app.models.kehadiran import Kehadiran
from app.models.berita_acara_perkuliahan import BeritaAcaraPerkuliahan
from app.models.kelas_mahasiswa import KelasMahasiswa
from app.models.mahasiswa import Mahasiswa
from app.models.user import User
from app.schemas.kehadiran import (
    FaceRecognitionResponse,
    FaceRecognitionResult,
    KehadiranCreate,
    KehadiranResponse,
    KehadiranUpdate,
    RecognizedMahasiswa,
    StatusKehadiran,
)
from app.services.face_recognition import (
    FaceRecognitionService,
    FaceRecognitionUnavailable,
    InvalidImageError,
)
from app.utils.auth import get_current_user

router = APIRouter(prefix="/kehadiran", tags=["Kehadiran"])

logger = logging.getLogger(__name__)
settings = get_settings()

face_service = FaceRecognitionService(
    model_dir=settings.FACE_MODEL_DIR,
    method=settings.FACE_MODEL_METHOD,
    threshold=settings.FACE_RECOGNITION_THRESHOLD,
)


@router.get("/", response_model=List[KehadiranResponse])
def get_all_kehadiran(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    kehadiran = db.query(Kehadiran).offset(skip).limit(limit).all()
    return kehadiran


@router.get("/bap/{bap_id}", response_model=List[KehadiranResponse])
def get_kehadiran_by_bap(
    bap_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    kehadiran = db.query(Kehadiran).filter(Kehadiran.id_bap == bap_id).all()
    return kehadiran


@router.get("/mahasiswa/{mahasiswa_id}", response_model=List[KehadiranResponse])
def get_kehadiran_by_mahasiswa(
    mahasiswa_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    kehadiran = db.query(Kehadiran).filter(
        Kehadiran.id_mahasiswa == mahasiswa_id
    ).all()
    return kehadiran


@router.post("/recognize", response_model=FaceRecognitionResponse)
async def recognize_kehadiran(
    id_bap: int = Form(...),
    file: UploadFile = File(...),
    mode: Literal["single", "multi"] = Form("single"),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    bap = db.query(BeritaAcaraPerkuliahan).filter(
        BeritaAcaraPerkuliahan.id == id_bap
    ).first()

    if not bap:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Berita Acara Perkuliahan tidak ditemukan",
        )

    if file.content_type and not file.content_type.startswith("image/"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="File upload harus berupa gambar",
        )

    image_bytes = await file.read()

    if not image_bytes:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="File upload kosong",
        )

    try:
        recognized_faces = face_service.recognize(
            image_bytes=image_bytes,
            mode=mode,
        )

    except InvalidImageError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        ) from exc

    except FaceRecognitionUnavailable as exc:
        logger.exception("Face recognition unavailable")
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=str(exc),
        ) from exc

    except Exception as exc:
        logger.exception("Face recognition failed")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Gagal memproses absensi wajah",
        ) from exc

    now_time = datetime.now().time()
    batas_waktu = bap.waktu_selesai

    status_absen = (
        StatusKehadiran.TERLAMBAT.value
        if batas_waktu and now_time > batas_waktu
        else StatusKehadiran.HADIR.value
    )

    keterangan_absen = (
        "Mahasiswa hadir setelah waktu selesai"
        if status_absen == StatusKehadiran.TERLAMBAT.value
        else "Dicatat otomatis dari absensi wajah"
    )

    class_has_members = db.query(KelasMahasiswa).filter(
        KelasMahasiswa.kelas_id == bap.id_kelas
    ).first() is not None

    results: List[FaceRecognitionResult] = []
    changed_records: List[Kehadiran] = []

    for face in recognized_faces:
        if not face.nim:
            results.append(
                _build_recognition_result(
                    face=face,
                    status_text="low_confidence",
                    message="Confidence di bawah threshold, kehadiran tidak dicatat",
                )
            )
            continue

        mahasiswa = db.query(Mahasiswa).filter(
            Mahasiswa.nim == face.nim
        ).first()

        if not mahasiswa:
            results.append(
                _build_recognition_result(
                    face=face,
                    status_text="unregistered",
                    message="Mahasiswa tidak ditemukan di database",
                )
            )
            continue

        if class_has_members:
            membership = db.query(KelasMahasiswa).filter(
                KelasMahasiswa.kelas_id == bap.id_kelas,
                KelasMahasiswa.mahasiswa_id == mahasiswa.id_mahasiswa,
            ).first()

            if not membership:
                results.append(
                    _build_recognition_result(
                        face=face,
                        mahasiswa=mahasiswa,
                        status_text="not_in_class",
                        message="Mahasiswa tidak terdaftar pada kelas BAP",
                    )
                )
                continue

        existing = db.query(Kehadiran).filter(
            Kehadiran.id_bap == id_bap,
            Kehadiran.id_mahasiswa == mahasiswa.id_mahasiswa,
        ).first()

        if existing:
            if existing.status != status_absen:
                existing.status = status_absen
                existing.keterangan = keterangan_absen
                changed_records.append(existing)

                status_text = "updated"
                message = f"Kehadiran diperbarui menjadi {status_absen}"
            else:
                status_text = "already_recorded"
                message = f"Kehadiran sudah tercatat sebagai {status_absen}"

            kehadiran = existing

        else:
            kehadiran = Kehadiran(
                id_bap=id_bap,
                id_mahasiswa=mahasiswa.id_mahasiswa,
                status=status_absen,
                keterangan=keterangan_absen,
            )

            db.add(kehadiran)
            changed_records.append(kehadiran)

            status_text = "recorded"
            message = f"Kehadiran berhasil dicatat sebagai {status_absen}"

        results.append(
            _build_recognition_result(
                face=face,
                mahasiswa=mahasiswa,
                status_text=status_text,
                message=message,
                kehadiran=kehadiran,
            )
        )

    if changed_records:
        db.commit()

        for record in changed_records:
            db.refresh(record)

        for result in results:
            if result.kehadiran_id is None and result.mahasiswa is not None:
                record = db.query(Kehadiran).filter(
                    Kehadiran.id_bap == id_bap,
                    Kehadiran.id_mahasiswa == result.mahasiswa.id_mahasiswa,
                ).first()

                if record:
                    result.kehadiran_id = record.id
    else:
        db.rollback()

    return FaceRecognitionResponse(
        id_bap=id_bap,
        mode=mode,
        results=results,
    )


def _build_recognition_result(
    face,
    status_text: str,
    message: str,
    mahasiswa: Optional[Mahasiswa] = None,
    kehadiran: Optional[Kehadiran] = None,
) -> FaceRecognitionResult:
    return FaceRecognitionResult(
        face_index=face.face_index,
        nim=face.nim,
        mahasiswa=RecognizedMahasiswa.model_validate(mahasiswa)
        if mahasiswa
        else None,
        confidence=face.confidence,
        detection_confidence=face.detection_confidence,
        bbox=face.bbox,
        status=status_text,
        kehadiran_id=kehadiran.id if kehadiran else None,
        message=message,
    )


@router.get("/{kehadiran_id}", response_model=KehadiranResponse)
def get_kehadiran(
    kehadiran_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    kehadiran = db.query(Kehadiran).filter(Kehadiran.id == kehadiran_id).first()

    if not kehadiran:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Kehadiran tidak ditemukan",
        )

    return kehadiran


@router.post("/", response_model=KehadiranResponse, status_code=status.HTTP_201_CREATED)
def create_kehadiran(
    kehadiran_data: KehadiranCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    bap = db.query(BeritaAcaraPerkuliahan).filter(
        BeritaAcaraPerkuliahan.id == kehadiran_data.id_bap
    ).first()

    if not bap:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Berita Acara Perkuliahan tidak ditemukan",
        )

    mahasiswa = db.query(Mahasiswa).filter(
        Mahasiswa.id_mahasiswa == kehadiran_data.id_mahasiswa
    ).first()

    if not mahasiswa:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Mahasiswa tidak ditemukan",
        )

    existing = db.query(Kehadiran).filter(
        Kehadiran.id_bap == kehadiran_data.id_bap,
        Kehadiran.id_mahasiswa == kehadiran_data.id_mahasiswa,
    ).first()

    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Kehadiran untuk mahasiswa ini sudah tercatat",
        )

    kehadiran = Kehadiran(**kehadiran_data.model_dump())

    db.add(kehadiran)
    db.commit()
    db.refresh(kehadiran)

    return kehadiran


@router.put("/{kehadiran_id}", response_model=KehadiranResponse)
def update_kehadiran(
    kehadiran_id: int,
    kehadiran_data: KehadiranUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    kehadiran = db.query(Kehadiran).filter(Kehadiran.id == kehadiran_id).first()

    if not kehadiran:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Kehadiran tidak ditemukan",
        )

    update_data = kehadiran_data.model_dump(exclude_unset=True)

    if not update_data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Tidak ada data yang diupdate. Minimal satu field harus diisi.",
        )

    has_changes = False

    for field, value in update_data.items():
        if getattr(kehadiran, field) != value:
            has_changes = True
            setattr(kehadiran, field, value)

    if not has_changes:
        return kehadiran

    db.commit()
    db.refresh(kehadiran)

    return kehadiran


@router.delete("/{kehadiran_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_kehadiran(
    kehadiran_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    kehadiran = db.query(Kehadiran).filter(Kehadiran.id == kehadiran_id).first()

    if not kehadiran:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Kehadiran tidak ditemukan",
        )

    db.delete(kehadiran)
    db.commit()

    return None