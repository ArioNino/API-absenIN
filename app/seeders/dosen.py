from app.models.kelas import Kelas
from app.seeders.base import BaseSeeder


class Dosen(BaseSeeder):
    DATA = [
        (2)
    ]

    def seed(self):
        for id_user in self.DATA:
            exists = self.db.query(Dosen).filter(Dosen.id_user == id_user).first()
            if exists:
                self.skipped += 1
                continue
            dosen = Dosen(id_user=id_user)
            self.db.add(dosen)
            self.inserted += 1
        self.db.commit()
