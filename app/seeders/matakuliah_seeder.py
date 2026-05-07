from app.models.matakuliah import MataKuliah
from app.seeders.base import BaseSeeder


class MataKuliahSeeder(BaseSeeder):
    DATA = [
        ("KOM0001", "Pemrograman Dasar", 3, 1),
        ("KOM0002", "Struktur Data", 3, 2),
        ("KOM0003", "Algoritma dan Pemrograman", 4, 2),
        ("KOM0004", "Basis Data", 3, 3),
        ("KOM0005", "Sistem Operasi", 3, 3),
        ("KOM0006", "Jaringan Komputer", 3, 4),
        ("KOM0007", "Rekayasa Perangkat Lunak", 4, 4),
        ("KOM0008", "Keamanan Siber", 3, 5),
    ]

    def seed(self):
        for kode_mk, nama_mk, sks, semester in self.DATA:
            exists = self.db.query(MataKuliah).filter(
                MataKuliah.kode_mk == kode_mk
            ).first()
            if exists:
                self.skipped += 1
                continue
            mk = MataKuliah(
                kode_mk=kode_mk,
                nama_mk=nama_mk,
                sks=sks,
                semester=semester
            )
            self.db.add(mk)
            self.inserted += 1
        self.db.commit()
