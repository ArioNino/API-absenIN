from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Kelas(Base):
    __tablename__ = "kelas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nama_kelas = Column(String(50), nullable=False)

    # Relationships
    berita_acara = relationship("BeritaAcaraPerkuliahan", back_populates="kelas")
    kelas_mahasiswa = relationship("KelasMahasiswa", back_populates="kelas")
    kelas_dosen = relationship("Kelas_dosen", back_populates="kelas")
