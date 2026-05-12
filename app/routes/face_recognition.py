import traceback
from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.mahasiswa import Mahasiswa
from app.services.face_recognition import (
    FaceRecognitionService,
    FaceRecognitionUnavailable,
    InvalidImageError,
)

router = APIRouter(
    prefix="/face-recognition",
    tags=["Face Recognition"]
)

face_service = FaceRecognitionService(
    model_dir="model",
    method="yolo",
    threshold=0.6
)

@router.post("/recognize")
async def recognize_face(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    try:
        image_bytes = await file.read()

        if not image_bytes:
            raise HTTPException(status_code=400, detail="File gambar kosong")

        results = face_service.recognize(
            image_bytes=image_bytes,
            mode="single"
        )

        data = []

        for face in results:
            mahasiswa = None

            if face.nim:
                mahasiswa = db.query(Mahasiswa).filter(
                    Mahasiswa.nim == face.nim
                ).first()

            data.append({
                "face_index": face.face_index,
                "nim": face.nim,
                "nama": mahasiswa.nama if mahasiswa else None,
                "prodi": mahasiswa.prodi if mahasiswa else None,
                "confidence": face.confidence,
                "detection_confidence": face.detection_confidence,
                "bbox": face.bbox,
                "recognized": face.nim is not None,
                "mahasiswa_found": mahasiswa is not None
            })

        return {
            "success": True,
            "total_faces": len(data),
            "data": data
        }

    except InvalidImageError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except FaceRecognitionUnavailable as e:
        print("\n========== FACE RECOGNITION UNAVAILABLE ==========")
        traceback.print_exc()
        print("==================================================\n")
        raise HTTPException(status_code=500, detail=str(e))

    except Exception as e:
        print("\n========== FACE RECOGNITION ERROR ==========")
        traceback.print_exc()
        print("===========================================\n")
        raise HTTPException(status_code=500, detail=str(e))