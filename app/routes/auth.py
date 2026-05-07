from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.user import User
from app.schemas.user import LoginSchema
from app.utils.security import verify_password

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/login")
def login(data: LoginSchema, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == data.email).first()

    if not user:
        return {
        "status": "error", 
        "message": "Email tidak ditemukan"}

    if not verify_password(data.password, user.password):
        return {
            "status": "error", 
            "message": "Password salah"}

    return {
        "status": "success",
        "user": {
            "id": user.id,
            "email": user.email,
            "name": user.name
        }
    }