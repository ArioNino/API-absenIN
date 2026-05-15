from pydantic import BaseModel
from typing import List, Optional
from enum import Enum


class StatusKehadiran(str, Enum):
    HADIR = "Hadir"
    TERLAMBAT = "Terlambat"
    IZIN = "Izin"
    SAKIT = "Sakit"
    ALPHA = "Alpha"


class KehadiranBase(BaseModel):
    id_bap: int
    id_mahasiswa: int
    status: StatusKehadiran
    keterangan: Optional[str] = None


class KehadiranCreate(KehadiranBase):
    pass


class KehadiranUpdate(BaseModel):
    status: Optional[StatusKehadiran] = None
    keterangan: Optional[str] = None


class KehadiranResponse(KehadiranBase):
    id: int
    
    class Config:
        from_attributes = True


class RecognizedMahasiswa(BaseModel):
    id_mahasiswa: int
    nim: str
    nama: Optional[str] = None
    kelas: Optional[str] = None
    prodi: Optional[str] = None

    class Config:
        from_attributes = True


class FaceRecognitionResult(BaseModel):
    face_index: int
    nim: Optional[str] = None
    mahasiswa: Optional[RecognizedMahasiswa] = None
    confidence: float
    detection_confidence: Optional[float] = None
    bbox: Optional[List[float]] = None
    status: str
    kehadiran_id: Optional[int] = None
    message: str


class FaceRecognitionResponse(BaseModel):
    id_bap: int
    mode: str
    results: List[FaceRecognitionResult]
