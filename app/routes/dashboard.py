from datetime import date
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.models.mahasiswa import Mahasiswa
from app.models.kelas import Kelas
from app.models.kehadiran import Kehadiran
from app.models.berita_acara_perkuliahan import BeritaAcaraPerkuliahan
from app.utils.auth import get_current_user

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


@router.get("/stats")
def get_dashboard_stats(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    total_mahasiswa = db.query(Mahasiswa).count()
    total_kelas = db.query(Kelas).count()
    total_bap = db.query(BeritaAcaraPerkuliahan).count()

    today = date.today()

    total_today = (
        db.query(Kehadiran)
        .join(
            BeritaAcaraPerkuliahan,
            Kehadiran.id_bap == BeritaAcaraPerkuliahan.id,
        )
        .filter(BeritaAcaraPerkuliahan.tanggal == today)
        .count()
    )

    hadir_today = (
        db.query(Kehadiran)
        .join(
            BeritaAcaraPerkuliahan,
            Kehadiran.id_bap == BeritaAcaraPerkuliahan.id,
        )
        .filter(
            BeritaAcaraPerkuliahan.tanggal == today,
            Kehadiran.status == "Hadir",
        )
        .count()
    )

    attendance_rate = 0
    if total_today > 0:
        attendance_rate = round((hadir_today / total_today) * 100)

    return {
        "total_mahasiswa": total_mahasiswa,
        "total_kelas": total_kelas,
        "total_bap": total_bap,
        "attendance_rate": attendance_rate,
    }


@router.get("/today")
def get_today_attendance(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    today = date.today()

    bap_list = (
        db.query(BeritaAcaraPerkuliahan)
        .filter(BeritaAcaraPerkuliahan.tanggal == today)
        .all()
    )

    result = []

    for bap in bap_list:
        hadir_count = (
            db.query(Kehadiran)
            .filter(
                Kehadiran.id_bap == bap.id,
                Kehadiran.status == "Hadir",
            )
            .count()
        )

        total_count = (
            db.query(Kehadiran)
            .filter(Kehadiran.id_bap == bap.id)
            .count()
        )

        result.append(
            {
                "id": bap.id,
                "mata_kuliah": bap.mata_kuliah.nama_mk if bap.mata_kuliah else "-",
                "kelas": bap.kelas.nama_kelas if bap.kelas else "-",
                "waktu_mulai": str(bap.waktu_mulai),
                "waktu_selesai": str(bap.waktu_selesai),
                "hadir": hadir_count,
                "total": total_count,
            }
        )

    return result


@router.get("/status-distribution")
def get_status_distribution(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    statuses = ["Hadir", "Terlambat", "Izin", "Sakit", "Alpha"]

    result = []

    for item in statuses:
        total = db.query(Kehadiran).filter(Kehadiran.status == item).count()

        result.append(
            {
                "status": item,
                "total": total,
            }
        )

    return result