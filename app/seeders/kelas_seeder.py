from app.models.kelas import Kelas
from app.seeders.base import BaseSeeder


class KelasSeeder(BaseSeeder):
    DATA = [
        ("A", 1, "2023/2024", "KOM0001"),
        ("B", 1, "2023/2024", "KOM0001"),
        ("C", 2, "2023/2024", "KOM0002"),
        ("D", 2, "2023/2024", "KOM0003"),
        ("E", 3, "2023/2024", "KOM0004"),
        ("F", 4, "2023/2024", "KOM0006"),
    ]

    def seed(self):
        for nama_kelas, semester, tahun_ajaran, kode_mk in self.DATA:
            exists = self.db.query(Kelas).filter(
                Kelas.nama_kelas == nama_kelas,
                Kelas.tahun_ajaran == tahun_ajaran
            ).first()
            if exists:
                self.skipped += 1
                continue
            k = Kelas(
                nama_kelas=nama_kelas,
                semester=semester,
                tahun_ajaran=tahun_ajaran,
                kode_mk=kode_mk
            )
            self.db.add(k)
            self.inserted += 1
        self.db.commit()
