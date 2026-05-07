from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from app.database import Base


class Kehadiran(Base):
    __tablename__ = "kehadiran"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_bap = Column(Integer, ForeignKey("berita_acara_perkuliahan.id"), nullable=False)
    id_mahasiswa = Column(Integer, ForeignKey("mahasiswa.id_mahasiswa"), nullable=False)
    status = Column(String(20), nullable=False)
    keterangan = Column(Text, nullable=True)
    
    # Relationships
    berita_acara = relationship("BeritaAcaraPerkuliahan", back_populates="kehadiran")
    mahasiswa = relationship("Mahasiswa", back_populates="kehadiran")
