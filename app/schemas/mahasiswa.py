from pydantic import BaseModel, Field, field_validator
from typing import Optional


class MahasiswaBase(BaseModel):
    nim: str = Field(
        ...,
        description="NIM mahasiswa (11 karakter)",
        min_length=1,
        max_length=11,
        examples=["J0403231999"],
    )
    nama: str = Field(
        ...,
        description="Nama lengkap mahasiswa",
        min_length=1,
        examples=["NAMA MAHASISWA"],
    )
    prodi: str = Field(
        ...,
        description="Program studi (TRPL, JMP, dll)",
        min_length=1,
        examples=["TRPL"],
    )

    @field_validator("nim")
    @classmethod
    def validate_nim(cls, v: str) -> str:
        if not v or v.strip() == "":
            raise ValueError("NIM tidak boleh kosong")
        return v.strip()

    @field_validator("nama")
    @classmethod
    def validate_nama(cls, v: str) -> str:
        if not v or v.strip() == "":
            raise ValueError("Nama tidak boleh kosong")
        return v.strip()

    @field_validator("prodi")
    @classmethod
    def validate_prodi(cls, v: str) -> str:
        if not v or v.strip() == "":
            raise ValueError("Prodi tidak boleh kosong")
        return v.strip()


class MahasiswaCreate(MahasiswaBase):
    pass


class MahasiswaUpdate(BaseModel):
    nim: Optional[str] = Field(
        None,
        description="NIM mahasiswa",
        examples=["J0403231999"],
    )
    nama: Optional[str] = Field(
        None,
        description="Nama lengkap mahasiswa",
        examples=["NAMA MAHASISWA"],
    )
    prodi: Optional[str] = Field(
        None,
        description="Program studi",
        examples=["TRPL"],
    )


class MahasiswaResponse(MahasiswaBase):
    id_mahasiswa: int
    id_kelas: Optional[int] = None
    nama_kelas: Optional[str] = None

    class Config:
        from_attributes = True


class MessageResponse(BaseModel):
    message: str
    data: Optional[MahasiswaResponse] = None


class DeleteResponse(BaseModel):
    message: str
    deleted_id: int