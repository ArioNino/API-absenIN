from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Mahasiswa(Base):
    __tablename__ = "mahasiswa"
    
    id_mahasiswa = Column(Integer, primary_key=True, index=True)
    nim = Column(String(11), unique=True, nullable=False)
    nama = Column(String(100))
    # kelas = Column(String(100))
    prodi = Column(String(100))
    
    # Relationships
    kehadiran = relationship("Kehadiran", back_populates="mahasiswa")
    kelas_mahasiswa = relationship("KelasMahasiswa", back_populates="mahasiswa")