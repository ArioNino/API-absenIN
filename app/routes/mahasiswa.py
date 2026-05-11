from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.mahasiswa import Mahasiswa
from app.models.user import User
from app.schemas.mahasiswa import (
    MahasiswaCreate, 
    MahasiswaUpdate, 
    MahasiswaResponse,
    MessageResponse,
    DeleteResponse
)
from app.utils.auth import get_current_user

router = APIRouter(prefix="/mahasiswa", tags=["Mahasiswa"])


@router.get("/", response_model=List[MahasiswaResponse])
def get_all_mahasiswa(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get all mahasiswa with pagination."""
    mahasiswa = db.query(Mahasiswa).offset(skip).limit(limit).all()
    return mahasiswa


@router.get("/nim/{nim}", response_model=MahasiswaResponse)
def get_mahasiswa_by_nim(
    nim: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get a specific mahasiswa by NIM."""
    mahasiswa = db.query(Mahasiswa).filter(Mahasiswa.nim == nim).first()
    if not mahasiswa:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Mahasiswa tidak ditemukan"
        )
    return mahasiswa


@router.get("/{mahasiswa_id}", response_model=MahasiswaResponse)
def get_mahasiswa(
    mahasiswa_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get a specific mahasiswa by ID."""
    mahasiswa = db.query(Mahasiswa).filter(Mahasiswa.id_mahasiswa == mahasiswa_id).first()
    if not mahasiswa:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Mahasiswa tidak ditemukan"
        )
    return mahasiswa


@router.post("/", response_model=MessageResponse, status_code=status.HTTP_201_CREATED)
def create_mahasiswa(
    mahasiswa_data: MahasiswaCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Create a new mahasiswa."""
    # Check if NIM already exists
    existing = db.query(Mahasiswa).filter(Mahasiswa.nim == mahasiswa_data.nim).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="NIM sudah terdaftar"
        )
    
    mahasiswa = Mahasiswa(**mahasiswa_data.model_dump())
    db.add(mahasiswa)
    db.commit()
    db.refresh(mahasiswa)
    
    return MessageResponse(
        message="Mahasiswa berhasil ditambahkan",
        data=MahasiswaResponse.model_validate(mahasiswa)
    )


@router.put("/{mahasiswa_id}", response_model=MessageResponse)
def update_mahasiswa(
    mahasiswa_id: int,
    mahasiswa_data: MahasiswaUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Update a mahasiswa."""
    mahasiswa = db.query(Mahasiswa).filter(Mahasiswa.id_mahasiswa == mahasiswa_id).first()
    if not mahasiswa:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Mahasiswa tidak ditemukan"
        )
    
    # Get update data
    update_data = mahasiswa_data.model_dump(exclude_unset=True)
    
    # Check if there's any data to update (dirty check)
    if not update_data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Tidak ada data yang diupdate. Minimal satu field harus diisi."
        )
    
    # Check if new NIM already exists (if NIM is being updated)
    if mahasiswa_data.nim and mahasiswa_data.nim != mahasiswa.nim:
        existing = db.query(Mahasiswa).filter(Mahasiswa.nim == mahasiswa_data.nim).first()
        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="NIM sudah terdaftar"
            )
    
    # Update fields
    for field, value in update_data.items():
        setattr(mahasiswa, field, value)
    
    db.commit()
    db.refresh(mahasiswa)
    
    return MessageResponse(
        message="Mahasiswa berhasil diupdate",
        data=MahasiswaResponse.model_validate(mahasiswa)
    )


@router.delete("/{mahasiswa_id}", response_model=DeleteResponse)
def delete_mahasiswa(
    mahasiswa_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Delete a mahasiswa."""
    mahasiswa = db.query(Mahasiswa).filter(Mahasiswa.id_mahasiswa == mahasiswa_id).first()
    if not mahasiswa:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Mahasiswa tidak ditemukan"
        )
    
    db.delete(mahasiswa)
    db.commit()
    
    return DeleteResponse(
        message="Mahasiswa berhasil dihapus",
        deleted_id=mahasiswa_id
    )
