from pydantic import BaseModel
from typing import Optional


class KelasBase(BaseModel):
    nama_kelas: str
    semester: int
    tahun_ajaran: str
    kode_mk: str


class KelasCreate(KelasBase):
    pass


class KelasUpdate(BaseModel):
    nama_kelas: Optional[str] = None
    semester: Optional[int] = None
    tahun_ajaran: Optional[str] = None
    kode_mk: Optional[str] = None


class KelasResponse(KelasBase):
    id: int
    
    class Config:
        from_attributes = True
