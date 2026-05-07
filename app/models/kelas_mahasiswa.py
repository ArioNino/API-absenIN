from sqlalchemy import Column, ForeignKey, Integer, String
from app.database import Base

class KelasMahasiswa(Base):
    __tablename__ = "kelas_mahasiswa"

    id_kelas_mahasiswa = Column(Integer, primary_key=True, index=True)
    mahasiswa_id = Column(Integer, ForeignKey("mahasiswa.id_mahasiswa"), nullable=False)