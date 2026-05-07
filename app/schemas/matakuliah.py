from pydantic import BaseModel, Field
from typing import Optional


class MataKuliahBase(BaseModel):
    kode_mk: str = Field(..., description="Kode mata kuliah (max 10 karakter)", min_length=1, max_length=10)
    nama_mk: str = Field(..., description="Nama mata kuliah", min_length=1)
    sks: int = Field(..., description="Jumlah SKS", ge=1, le=6)
    semester: int = Field(..., description="Semester", ge=1, le=8)


class MataKuliahCreate(MataKuliahBase):
    pass


class MataKuliahUpdate(BaseModel):
    nama_mk: Optional[str] = Field(None, description="Nama mata kuliah", min_length=1)
    sks: Optional[int] = Field(None, description="Jumlah SKS", ge=1, le=6)
    semester: Optional[int] = Field(None, description="Semester", ge=1, le=8)


class MataKuliahResponse(MataKuliahBase):
    
    class Config:
        from_attributes = True


class MessageResponse(BaseModel):
    """Generic message response"""
    message: str
    data: Optional[MataKuliahResponse] = None


class DeleteResponse(BaseModel):
    """Response for delete operations"""
    message: str
    deleted_kode: str
