from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class Kelas(Base):
    __tablename__ = "kelas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nama_kelas = Column(String(50), nullable=False)
    semester = Column(Integer, nullable=False)
    tahun_ajaran = Column(String(20), nullable=False)

    kode_mk = Column(String(10), ForeignKey("mata_kuliah.kode_mk"), nullable=False)