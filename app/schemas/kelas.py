from pydantic import BaseModel, Field
from typing import Optional


class KelasBase(BaseModel):
    nama_kelas: str = Field(..., description="Nama kelas", min_length=1, max_length=50)


class KelasCreate(KelasBase):
    pass


class KelasUpdate(BaseModel):
    nama_kelas: Optional[str] = Field(None, description="Nama kelas", min_length=1, max_length=50)


class KelasResponse(KelasBase):
    id: int

    class Config:
        from_attributes = True
