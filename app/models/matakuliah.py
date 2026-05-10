from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from app.database import Base

class MataKuliah(Base):
    __tablename__ = "mata_kuliah"

    kode_mk = Column(String(10), primary_key=True, nullable=False)
    nama_mk = Column(String(100), nullable=False)
    sks = Column(Integer, nullable=False)
    semester = Column(Integer, nullable=False)
    
    # Relationships
    berita_acara = relationship("BeritaAcaraPerkuliahan", back_populates="mata_kuliah")