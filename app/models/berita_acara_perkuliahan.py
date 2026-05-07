from sqlalchemy import Column, Date, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from app.database import Base

class BeritaAcaraPerkuliahan(Base):
    __tablename__ = "berita_acara_perkuliahan"

    id = Column(Integer, primary_key=True)
    id_dosen = Column(Integer, ForeignKey("dosen.id"), nullable=False)
    id_kelas = Column(Integer, ForeignKey("kelas.id"), nullable=False)
    id_mata_kuliah = Column(String(10), ForeignKey("mata_kuliah.kode_mk"), nullable=False)
    pertemuan_ke = Column(Integer, nullable=False)
    tanggal = Column(Date, nullable=False)
    materi = Column(String(255), nullable=False)
    catatan = Column(Text, nullable=True)
    
    # Relationships
    dosen = relationship("Dosen", back_populates="berita_acara")
    kelas = relationship("Kelas", back_populates="berita_acara")
    mata_kuliah = relationship("MataKuliah", back_populates="berita_acara")
    kehadiran = relationship("Kehadiran", back_populates="berita_acara")