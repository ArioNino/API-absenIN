from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.matakuliah import MataKuliah
from app.models.user import User
from app.schemas.matakuliah import (
    MataKuliahCreate, 
    MataKuliahUpdate, 
    MataKuliahResponse,
    MessageResponse,
    DeleteResponse
)
from app.utils.auth import get_current_user

router = APIRouter(prefix="/matakuliah", tags=["Mata Kuliah"])


@router.get("/", response_model=List[MataKuliahResponse])
def get_all_matakuliah(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get all mata kuliah with pagination."""
    matakuliah = db.query(MataKuliah).offset(skip).limit(limit).all()
    return matakuliah


@router.get("/{kode_mk}", response_model=MataKuliahResponse)
def get_matakuliah(
    kode_mk: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get a specific mata kuliah by kode."""
    matakuliah = db.query(MataKuliah).filter(MataKuliah.kode_mk == kode_mk).first()
    if not matakuliah:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Mata kuliah tidak ditemukan"
        )
    return matakuliah


@router.post("/", response_model=MessageResponse, status_code=status.HTTP_201_CREATED)
def create_matakuliah(
    matakuliah_data: MataKuliahCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Create a new mata kuliah."""
    # Check if kode_mk already exists
    existing = db.query(MataKuliah).filter(MataKuliah.kode_mk == matakuliah_data.kode_mk).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Kode mata kuliah sudah terdaftar"
        )
    
    matakuliah = MataKuliah(**matakuliah_data.model_dump())
    db.add(matakuliah)
    db.commit()
    db.refresh(matakuliah)
    
    return MessageResponse(
        message="Mata kuliah berhasil ditambahkan",
        data=MataKuliahResponse.model_validate(matakuliah)
    )


@router.put("/{kode_mk}", response_model=MessageResponse)
def update_matakuliah(
    kode_mk: str,
    matakuliah_data: MataKuliahUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Update a mata kuliah."""
    matakuliah = db.query(MataKuliah).filter(MataKuliah.kode_mk == kode_mk).first()
    if not matakuliah:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Mata kuliah tidak ditemukan"
        )
    
    # Check if there's any data to update (dirty check)
    update_data = matakuliah_data.model_dump(exclude_unset=True)
    if not update_data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Tidak ada data yang diupdate. Minimal satu field harus diisi."
        )
    
    # Check if any field actually changed
    has_changes = False
    for field, value in update_data.items():
        if getattr(matakuliah, field) != value:
            has_changes = True
            setattr(matakuliah, field, value)
    
    if not has_changes:
        # Idempotent no-op: payload matches current state, nothing to persist.
        return MessageResponse(
            message="Tidak ada perubahan data. Data yang dikirim sama dengan data yang ada.",
            data=MataKuliahResponse.model_validate(matakuliah)
        )
    
    db.commit()
    db.refresh(matakuliah)
    
    return MessageResponse(
        message="Mata kuliah berhasil diupdate",
        data=MataKuliahResponse.model_validate(matakuliah)
    )


@router.delete("/{kode_mk}", response_model=DeleteResponse)
def delete_matakuliah(
    kode_mk: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Delete a mata kuliah."""
    matakuliah = db.query(MataKuliah).filter(MataKuliah.kode_mk == kode_mk).first()
    if not matakuliah:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Mata kuliah tidak ditemukan"
        )
    
    db.delete(matakuliah)
    db.commit()
    
    return DeleteResponse(
        message="Mata kuliah berhasil dihapus",
        deleted_kode=kode_mk
    )
