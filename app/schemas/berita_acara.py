from pydantic import BaseModel
from typing import Optional
from datetime import date, time


class MataKuliahNested(BaseModel):
    kode_mk: str
    nama_mk: str

    class Config:
        from_attributes = True


class KelasNested(BaseModel):
    id: int
    nama_kelas: str

    class Config:
        from_attributes = True


class BeritaAcaraBase(BaseModel):
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
    mata_kuliah: Optional[MataKuliahNested] = None
    kelas: Optional[KelasNested] = None

    class Config:
        from_attributes = True