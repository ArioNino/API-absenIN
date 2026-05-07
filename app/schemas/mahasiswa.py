from pydantic import BaseModel, Field, field_validator
from typing import Optional


class MahasiswaBase(BaseModel):
    nim: str = Field(..., description="NIM mahasiswa (11 karakter)", min_length=1, max_length=11, examples=["J0403231999"])
    nama: str = Field(..., description="Nama lengkap mahasiswa", min_length=1, examples=["NAMA MAHASISWA"])
    kelas: str = Field(..., description="Kelas mahasiswa (A, B, C, dll)", min_length=1, examples=["A"])
    prodi: str = Field(..., description="Program studi (TRPL, JMP, dll)", min_length=1, examples=["TRPL"])
    
    @field_validator('nim')
    @classmethod
    def validate_nim(cls, v: str) -> str:
        if not v or v.strip() == "":
            raise ValueError('NIM tidak boleh kosong')
        return v.strip()
    
    @field_validator('nama')
    @classmethod
    def validate_nama(cls, v: str) -> str:
        if not v or v.strip() == "":
            raise ValueError('Nama tidak boleh kosong')
        return v.strip()
    
    @field_validator('kelas')
    @classmethod
    def validate_kelas(cls, v: str) -> str:
        if not v or v.strip() == "":
            raise ValueError('Kelas tidak boleh kosong')
        return v.strip()
    
    @field_validator('prodi')
    @classmethod
    def validate_prodi(cls, v: str) -> str:
        if not v or v.strip() == "":
            raise ValueError('Prodi tidak boleh kosong')
        return v.strip()


class MahasiswaCreate(MahasiswaBase):
    """
    Schema untuk membuat mahasiswa baru.
    
    Required fields:
    - nim: NIM mahasiswa (11 karakter)
    - nama: Nama lengkap mahasiswa
    - kelas: Kelas mahasiswa (A, B, C, dll)
    - prodi: Program studi (TRPL, JMP, dll)
    """
    pass


class MahasiswaUpdate(BaseModel):
    """
    Schema untuk update mahasiswa.
    
    Optional fields (isi yang ingin diubah saja):
    - nim: NIM mahasiswa
    - nama: Nama lengkap mahasiswa
    - kelas: Kelas mahasiswa
    - prodi: Program studi
    """
    nim: Optional[str] = Field(None, description="NIM mahasiswa", examples=["J0403231999"])
    nama: Optional[str] = Field(None, description="Nama lengkap mahasiswa", examples=["NAMA MAHASISWA"])
    kelas: Optional[str] = Field(None, description="Kelas mahasiswa", examples=["A"])
    prodi: Optional[str] = Field(None, description="Program studi", examples=["TRPL"])


class MahasiswaResponse(MahasiswaBase):
    id_mahasiswa: int
    
    class Config:
        from_attributes = True


class MessageResponse(BaseModel):
    """Generic message response"""
    message: str
    data: Optional[MahasiswaResponse] = None


class DeleteResponse(BaseModel):
    """Response for delete operations"""
    message: str
    deleted_id: int
