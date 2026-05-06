from sqlalchemy import Column, Integer, String
from app.database import Base

class Mahasiswa(Base):
    __tablename__ = "mahasiswa"
    
    id_mahasiswa = Column(Integer, primary_key=True, index=True)
    nim = Column(String(11), unique=True, nullable=False)
    nama = Column(String(100))
    kelas = Column(String(100))
    prodi = Column(String(100))