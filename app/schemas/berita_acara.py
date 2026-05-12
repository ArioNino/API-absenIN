from pydantic import BaseModel
from typing import Optional
from datetime import date, time

class BeritaAcaraBase(BaseModel):
    # id_dosen: int
    id_kelas: int
    id_mata_kuliah: str
    pertemuan_ke: int
    tanggal: date
    waktu_mulai: time
    waktu_selesai: time
    materi: str
    catatan: Optional[str] = None


class BeritaAcaraCreate(BeritaAcaraBase):
    pass


class BeritaAcaraUpdate(BaseModel):
    pertemuan_ke: Optional[int] = None
    tanggal: Optional[date] = None
    materi: Optional[str] = None
    catatan: Optional[str] = None


class BeritaAcaraResponse(BeritaAcaraBase):
    id: int
    
    class Config:
        from_attributes = True
