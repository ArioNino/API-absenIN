from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.berita_acara_perkuliahan import BeritaAcaraPerkuliahan
from app.models.dosen import Dosen
from app.models.kelas import Kelas
from app.models.matakuliah import MataKuliah
from app.models.user import User
from app.schemas.berita_acara import (
    BeritaAcaraCreate,
    BeritaAcaraUpdate,
    BeritaAcaraResponse
)
from app.utils.auth import get_current_user

router = APIRouter(prefix="/berita-acara", tags=["Berita Acara Perkuliahan"])


@router.get("/", response_model=List[BeritaAcaraResponse])
def get_all_berita_acara(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    berita_acara = db.query(BeritaAcaraPerkuliahan).offset(skip).limit(limit).all()
    return berita_acara


@router.get("/dosen/{dosen_id}", response_model=List[BeritaAcaraResponse])
def get_berita_acara_by_dosen(
    dosen_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    berita_acara = db.query(BeritaAcaraPerkuliahan).filter(
        BeritaAcaraPerkuliahan.id_dosen == dosen_id
    ).all()

    return berita_acara


@router.get("/kelas/{kelas_id}", response_model=List[BeritaAcaraResponse])
def get_berita_acara_by_kelas(
    kelas_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    berita_acara = db.query(BeritaAcaraPerkuliahan).filter(
        BeritaAcaraPerkuliahan.id_kelas == kelas_id
    ).all()

    return berita_acara


@router.get("/{bap_id}", response_model=BeritaAcaraResponse)
def get_berita_acara(
    bap_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    berita_acara = db.query(BeritaAcaraPerkuliahan).filter(
        BeritaAcaraPerkuliahan.id == bap_id
    ).first()

    if not berita_acara:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Berita Acara tidak ditemukan"
        )

    return berita_acara


@router.post("/", response_model=BeritaAcaraResponse, status_code=status.HTTP_201_CREATED)
def create_berita_acara(
    bap_data: BeritaAcaraCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    dosen = db.query(Dosen).filter(
        Dosen.id_user == current_user.id
    ).first()

    if not dosen:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Data dosen tidak ditemukan untuk user ini"
        )

    kelas = db.query(Kelas).filter(Kelas.id == bap_data.id_kelas).first()

    if not kelas:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Kelas tidak ditemukan"
        )

    mata_kuliah = db.query(MataKuliah).filter(
        MataKuliah.kode_mk == bap_data.id_mata_kuliah
    ).first()

    if not mata_kuliah:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Mata Kuliah tidak ditemukan"
        )

    existing = db.query(BeritaAcaraPerkuliahan).filter(
        BeritaAcaraPerkuliahan.id_kelas == bap_data.id_kelas,
        BeritaAcaraPerkuliahan.pertemuan_ke == bap_data.pertemuan_ke
    ).first()

    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Berita Acara untuk pertemuan ke-{bap_data.pertemuan_ke} sudah ada"
        )

    berita_acara = BeritaAcaraPerkuliahan(
        id_dosen=dosen.id,
        **bap_data.model_dump()
    )

    db.add(berita_acara)
    db.commit()
    db.refresh(berita_acara)

    return berita_acara


@router.put("/{bap_id}", response_model=BeritaAcaraResponse)
def update_berita_acara(
    bap_id: int,
    bap_data: BeritaAcaraUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    berita_acara = db.query(BeritaAcaraPerkuliahan).filter(
        BeritaAcaraPerkuliahan.id == bap_id
    ).first()

    if not berita_acara:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Berita Acara tidak ditemukan"
        )

    update_data = bap_data.model_dump(exclude_unset=True)

    if not update_data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Tidak ada data yang diupdate. Minimal satu field harus diisi."
        )

    for field, value in update_data.items():
        setattr(berita_acara, field, value)

    db.commit()
    db.refresh(berita_acara)

    return berita_acara


@router.delete("/{bap_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_berita_acara(
    bap_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    berita_acara = db.query(BeritaAcaraPerkuliahan).filter(
        BeritaAcaraPerkuliahan.id == bap_id
    ).first()

    if not berita_acara:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Berita Acara tidak ditemukan"
        )

    db.delete(berita_acara)
    db.commit()

    return None