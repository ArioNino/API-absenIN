from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True)
    password = Column(String(255))
    name = Column(String(100))
    
    # Relationships
    dosen = relationship("Dosen", back_populates="user", uselist=False)