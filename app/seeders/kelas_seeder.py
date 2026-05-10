from app.models.kelas import Kelas
from app.seeders.base import BaseSeeder


class KelasSeeder(BaseSeeder):
    DATA = [
        ("A",),
        ("B",),
        ("C",),
        ("D",),
        ("E",),
        ("F",),
    ]

    def seed(self):
        for (nama_kelas,) in self.DATA:
            exists = self.db.query(Kelas).filter(
                Kelas.nama_kelas == nama_kelas
            ).first()
            if exists:
                self.skipped += 1
                continue
            k = Kelas(nama_kelas=nama_kelas)
            self.db.add(k)
            self.inserted += 1
        self.db.commit()
