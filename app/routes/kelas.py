from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.kelas import Kelas
from app.models.matakuliah import MataKuliah
from app.models.user import User

from app.schemas.kelas import (
    KelasCreate,
    KelasUpdate,
    KelasResponse
)

from app.utils.auth import get_current_user

router = APIRouter(prefix="/kelas", tags=["Kelas"])


@router.get("/", response_model=List[KelasResponse])
def get_all_kelas(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get all kelas with pagination."""
    
    kelas = db.query(Kelas).offset(skip).limit(limit).all()
    return kelas


@router.get("/{kelas_id}", response_model=KelasResponse)
def get_kelas(
    kelas_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get a specific kelas by ID."""

    kelas = db.query(Kelas).filter(Kelas.id == kelas_id).first()

    if not kelas:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Kelas tidak ditemukan"
        )

    return kelas


@router.post("/", response_model=KelasResponse, status_code=status.HTTP_201_CREATED)
def create_kelas(
    kelas_data: KelasCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Create a new kelas."""

    # Check mata kuliah exists
    mata_kuliah = db.query(MataKuliah).filter(
        MataKuliah.kode_mk == kelas_data.kode_mk
    ).first()

    if not mata_kuliah:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Mata kuliah tidak ditemukan"
        )

    kelas = Kelas(**kelas_data.model_dump())

    db.add(kelas)
    db.commit()
    db.refresh(kelas)

    return kelas


@router.put("/{kelas_id}", response_model=KelasResponse)
def update_kelas(
    kelas_id: int,
    kelas_data: KelasUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Update kelas."""

    kelas = db.query(Kelas).filter(Kelas.id == kelas_id).first()

    if not kelas:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Kelas tidak ditemukan"
        )

    update_data = kelas_data.model_dump(exclude_unset=True)

    # Dirty check
    if not update_data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Tidak ada data yang diupdate"
        )

    # Check mata kuliah exists if kode_mk updated
    if "kode_mk" in update_data:
        mata_kuliah = db.query(MataKuliah).filter(
            MataKuliah.kode_mk == update_data["kode_mk"]
        ).first()

        if not mata_kuliah:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Mata kuliah tidak ditemukan"
            )

    # Update fields
    for field, value in update_data.items():
        setattr(kelas, field, value)

    db.commit()
    db.refresh(kelas)

    return kelas


@router.delete("/{kelas_id}")
def delete_kelas(
    kelas_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Delete kelas."""

    kelas = db.query(Kelas).filter(Kelas.id == kelas_id).first()

    if not kelas:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Kelas tidak ditemukan"
        )

    db.delete(kelas)
    db.commit()

    return {
        "message": "Kelas berhasil dihapus",
        "deleted_id": kelas_id
    }