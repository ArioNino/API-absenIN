from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload
from typing import List

from app.database import get_db
from app.models.mahasiswa import Mahasiswa
from app.models.user import User
from app.models.kelas_mahasiswa import KelasMahasiswa
from app.schemas.mahasiswa import (
    MahasiswaCreate,
    MahasiswaUpdate,
    MahasiswaResponse,
    MessageResponse,
    DeleteResponse,
)
from app.utils.auth import get_current_user

router = APIRouter(prefix="/mahasiswa", tags=["Mahasiswa"])


def mahasiswa_to_response(mahasiswa: Mahasiswa):
    id_kelas = None
    nama_kelas = None

    if mahasiswa.kelas_mahasiswa:
        relasi = mahasiswa.kelas_mahasiswa[0]

        if relasi.kelas:
            id_kelas = relasi.kelas.id
            nama_kelas = relasi.kelas.nama_kelas

    return {
        "id_mahasiswa": mahasiswa.id_mahasiswa,
        "nim": mahasiswa.nim,
        "nama": mahasiswa.nama,
        "prodi": mahasiswa.prodi,
        "id_kelas": id_kelas,
        "nama_kelas": nama_kelas,
    }


@router.get("/", response_model=List[MahasiswaResponse])
def get_all_mahasiswa(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    mahasiswa = (
        db.query(Mahasiswa)
        .options(
            joinedload(Mahasiswa.kelas_mahasiswa).joinedload(
                KelasMahasiswa.kelas
            )
        )
        .offset(skip)
        .limit(limit)
        .all()
    )

    return [mahasiswa_to_response(mhs) for mhs in mahasiswa]


@router.get("/nim/{nim}", response_model=MahasiswaResponse)
def get_mahasiswa_by_nim(
    nim: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    mahasiswa = (
        db.query(Mahasiswa)
        .options(
            joinedload(Mahasiswa.kelas_mahasiswa).joinedload(
                KelasMahasiswa.kelas
            )
        )
        .filter(Mahasiswa.nim == nim)
        .first()
    )

    if not mahasiswa:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Mahasiswa tidak ditemukan",
        )

    return mahasiswa_to_response(mahasiswa)


@router.get("/{mahasiswa_id}", response_model=MahasiswaResponse)
def get_mahasiswa(
    mahasiswa_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    mahasiswa = (
        db.query(Mahasiswa)
        .options(
            joinedload(Mahasiswa.kelas_mahasiswa).joinedload(
                KelasMahasiswa.kelas
            )
        )
        .filter(Mahasiswa.id_mahasiswa == mahasiswa_id)
        .first()
    )

    if not mahasiswa:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Mahasiswa tidak ditemukan",
        )

    return mahasiswa_to_response(mahasiswa)


@router.post("/", response_model=MessageResponse, status_code=status.HTTP_201_CREATED)
def create_mahasiswa(
    mahasiswa_data: MahasiswaCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    existing = db.query(Mahasiswa).filter(
        Mahasiswa.nim == mahasiswa_data.nim
    ).first()

    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="NIM sudah terdaftar",
        )

    mahasiswa = Mahasiswa(**mahasiswa_data.model_dump())

    db.add(mahasiswa)
    db.commit()
    db.refresh(mahasiswa)

    return MessageResponse(
        message="Mahasiswa berhasil ditambahkan",
        data=mahasiswa_to_response(mahasiswa),
    )


@router.put("/{mahasiswa_id}", response_model=MessageResponse)
def update_mahasiswa(
    mahasiswa_id: int,
    mahasiswa_data: MahasiswaUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    mahasiswa = db.query(Mahasiswa).filter(
        Mahasiswa.id_mahasiswa == mahasiswa_id
    ).first()

    if not mahasiswa:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Mahasiswa tidak ditemukan",
        )

    update_data = mahasiswa_data.model_dump(exclude_unset=True)

    if not update_data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Tidak ada data yang diupdate. Minimal satu field harus diisi.",
        )

    if mahasiswa_data.nim and mahasiswa_data.nim != mahasiswa.nim:
        existing = db.query(Mahasiswa).filter(
            Mahasiswa.nim == mahasiswa_data.nim
        ).first()

        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="NIM sudah terdaftar",
            )

    for field, value in update_data.items():
        setattr(mahasiswa, field, value)

    db.commit()
    db.refresh(mahasiswa)

    mahasiswa = (
        db.query(Mahasiswa)
        .options(
            joinedload(Mahasiswa.kelas_mahasiswa).joinedload(
                KelasMahasiswa.kelas
            )
        )
        .filter(Mahasiswa.id_mahasiswa == mahasiswa_id)
        .first()
    )

    return MessageResponse(
        message="Mahasiswa berhasil diupdate",
        data=mahasiswa_to_response(mahasiswa),
    )


@router.delete("/{mahasiswa_id}", response_model=DeleteResponse)
def delete_mahasiswa(
    mahasiswa_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    mahasiswa = db.query(Mahasiswa).filter(
        Mahasiswa.id_mahasiswa == mahasiswa_id
    ).first()

    if not mahasiswa:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Mahasiswa tidak ditemukan",
        )

    db.delete(mahasiswa)
    db.commit()

    return DeleteResponse(
        message="Mahasiswa berhasil dihapus",
        deleted_id=mahasiswa_id,
    )