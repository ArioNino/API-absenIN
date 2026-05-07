from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class KelasMahasiswa(Base):
    __tablename__ = "kelas_mahasiswa"

    id_kelas_mahasiswa = Column(Integer, primary_key=True, index=True)
    mahasiswa_id = Column(Integer, ForeignKey("mahasiswa.id_mahasiswa"), nullable=False)
    kelas_id = Column(Integer, ForeignKey("kelas.id"), nullable=False)
    
    # Relationships
    mahasiswa = relationship("Mahasiswa", back_populates="kelas_mahasiswa")
    kelas = relationship("Kelas", back_populates="kelas_mahasiswa")