# app/seeders/kelas_mahasiswa_seeder.py

from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.kelas_mahasiswa import KelasMahasiswa
from app.models.mahasiswa import Mahasiswa


class KelasMahasiswaSeeder:
    def __init__(self):
        self.db: Session = SessionLocal()
        self.created = 0

    def seed(self):

        # ambil mahasiswa prodi TRPL saja
        mahasiswa_list = (
            self.db.query(Mahasiswa)
            .filter(Mahasiswa.prodi == "TRPL")
            .all()
        )

        kelas_id = 1  # id kelas tujuan

        data = []

        for mahasiswa in mahasiswa_list:

            # cek duplicate
            existing = (
                self.db.query(KelasMahasiswa)
                .filter(
                    KelasMahasiswa.mahasiswa_id == mahasiswa.id_mahasiswa,
                    KelasMahasiswa.kelas_id == kelas_id
                )
                .first()
            )

            if not existing:
                data.append(
                    KelasMahasiswa(
                        mahasiswa_id=mahasiswa.id_mahasiswa,
                        kelas_id=kelas_id
                    )
                )

        self.db.add_all(data)
        self.db.commit()

        self.created = len(data)

    def report(self):
        return f"{self.created} mahasiswa TRPL berhasil dimasukkan ke kelas"

    def close(self):
        self.db.close()