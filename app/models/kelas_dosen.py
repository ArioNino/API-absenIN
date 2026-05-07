# from sqlalchemy import Column, ForeignKey, Integer, String
# from app.database import Base

# class Kelas_dosen(Base):
#     __tablename__ = "kelas_dosen"

#     id_kelas_dosen = Column(Integer, primary_key=True, index=True)
#     dosen_id = Column(Integer, ForeignKey("dosen.id_dosen"), nullable=False)