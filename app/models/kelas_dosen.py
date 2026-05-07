from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Kelas_dosen(Base):
    __tablename__ = "kelas_dosen"

    id_kelas_dosen = Column(Integer, primary_key=True, index=True)
    dosen_id = Column(Integer, ForeignKey("dosen.id"), nullable=False)
    kelas_id = Column(Integer, ForeignKey("kelas.id"), nullable=False)
    
    # Relationships
    dosen = relationship("Dosen", back_populates="kelas_dosen")
    kelas = relationship("Kelas", back_populates="kelas_dosen")