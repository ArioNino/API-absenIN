from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from app.database import Base


class Dosen(Base):
    __tablename__ = "dosen"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_user = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # Relationships
    user = relationship("User", back_populates="dosen")
    berita_acara = relationship("BeritaAcaraPerkuliahan", back_populates="dosen")
    kelas_dosen = relationship("Kelas_dosen", back_populates="dosen")
