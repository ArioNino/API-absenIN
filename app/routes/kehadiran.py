from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.kehadiran import Kehadiran
from app.models.berita_acara_perkuliahan import BeritaAcaraPerkuliahan
from app.models.mahasiswa import Mahasiswa
from app.models.user import User
from app.schemas.kehadiran import KehadiranCreate, KehadiranUpdate, KehadiranResponse
from app.utils.auth import get_current_user

router = APIRouter(prefix="/kehadiran", tags=["Kehadiran"])


@router.get("/", response_model=List[KehadiranResponse])
def get_all_kehadiran(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get all kehadiran records with pagination."""
    kehadiran = db.query(Kehadiran).offset(skip).limit(limit).all()
    return kehadiran


@router.get("/bap/{bap_id}", response_model=List[KehadiranResponse])
def get_kehadiran_by_bap(
    bap_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get all kehadiran for a specific BAP (lecture session)."""
    kehadiran = db.query(Kehadiran).filter(Kehadiran.id_bap == bap_id).all()
    return kehadiran


@router.get("/mahasiswa/{mahasiswa_id}", response_model=List[KehadiranResponse])
def get_kehadiran_by_mahasiswa(
    mahasiswa_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get all kehadiran for a specific mahasiswa."""
    kehadiran = db.query(Kehadiran).filter(Kehadiran.id_mahasiswa == mahasiswa_id).all()
    return kehadiran


@router.get("/{kehadiran_id}", response_model=KehadiranResponse)
def get_kehadiran(
    kehadiran_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get a specific kehadiran record."""
    kehadiran = db.query(Kehadiran).filter(Kehadiran.id == kehadiran_id).first()
    if not kehadiran:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Kehadiran tidak ditemukan"
        )
    return kehadiran


@router.post("/", response_model=KehadiranResponse, status_code=status.HTTP_201_CREATED)
def create_kehadiran(
    kehadiran_data: KehadiranCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Create a new kehadiran record."""
    # Verify BAP exists
    bap = db.query(BeritaAcaraPerkuliahan).filter(
        BeritaAcaraPerkuliahan.id == kehadiran_data.id_bap
    ).first()
    if not bap:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Berita Acara Perkuliahan tidak ditemukan"
        )
    
    # Verify mahasiswa exists
    mahasiswa = db.query(Mahasiswa).filter(
        Mahasiswa.id_mahasiswa == kehadiran_data.id_mahasiswa
    ).first()
    if not mahasiswa:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Mahasiswa tidak ditemukan"
        )
    
    # Check if kehadiran already exists for this BAP and mahasiswa
    existing = db.query(Kehadiran).filter(
        Kehadiran.id_bap == kehadiran_data.id_bap,
        Kehadiran.id_mahasiswa == kehadiran_data.id_mahasiswa
    ).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Kehadiran untuk mahasiswa ini sudah tercatat"
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
    current_user: User = Depends(get_current_user)
):
    """Update a kehadiran record."""
    kehadiran = db.query(Kehadiran).filter(Kehadiran.id == kehadiran_id).first()
    if not kehadiran:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Kehadiran tidak ditemukan"
        )
    
    # Check if there's any data to update (dirty check)
    update_data = kehadiran_data.model_dump(exclude_unset=True)
    if not update_data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Tidak ada data yang diupdate. Minimal satu field harus diisi."
        )
    
    # Check if any field actually changed
    has_changes = False
    for field, value in update_data.items():
        if getattr(kehadiran, field) != value:
            has_changes = True
            setattr(kehadiran, field, value)
    
    if not has_changes:
        # Idempotent no-op: payload matches current state, nothing to persist.
        return kehadiran
    
    db.commit()
    db.refresh(kehadiran)
    return kehadiran


@router.delete("/{kehadiran_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_kehadiran(
    kehadiran_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Delete a kehadiran record."""
    kehadiran = db.query(Kehadiran).filter(Kehadiran.id == kehadiran_id).first()
    if not kehadiran:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Kehadiran tidak ditemukan"
        )
    
    db.delete(kehadiran)
    db.commit()
    return None
