from pydantic import BaseModel
from typing import Optional
from enum import Enum


class StatusKehadiran(str, Enum):
    HADIR = "Hadir"
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
