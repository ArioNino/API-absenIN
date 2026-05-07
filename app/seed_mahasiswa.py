from app.database import SessionLocal
from app.models.mahasiswa import Mahasiswa

DATA = [
    ("J0403231006", "AZZAHRA NABILA CHAIRONA", "A", "TRPL"),
    ("J0403231019", "KEVIN FARHAN HERNANDEZ", "B", "TRPL"),
    ("J0403231031", "PUTI AISYAH LAILATULRAHMI", "A", "TRPL"),
    ("J0403231035", "ARIO ELNINO", "B", "TRPL"),
    ("J0403231041", "Nika Rani Nur Shafa Lubis", "A", "TRPL"),
    ("J0403231056", "Khinanti Angelita Puteri", "B", "TRPL"),
    ("J0403231061", "MUHAMMAD RAIHAN ZALDIPUTRA", "A", "TRPL"),
    ("J0403231094", "Faliana Alifia", "B", "TRPL"),
    ("J0403231132", "Jonathan", "A", "TRPL"),
    ("J0403231166", "GHANIYY FATTAH RAMADHAN", "B", "TRPL"),
    ("J0405231059", "MUHAMMAD FAKHRI HAKIM", "A", "JMP"),
    ("J0410231051", "Sarah Nahdiyatul Hasanah", "B", "JMP"),
    ("J0410231092", "Achmad Fauzan Wicaksono", "A", "JMP"),
    ("J0410231105", "Arta Novriana Napitupulu", "B", "JMP"),
    ("J0410231121", "ALYA YUNISA AULIAWATI", "A", "JMP"),
    ("J0410231154", "Dara Dynanti", "B", "JMP"),
]


def seed():
    db = SessionLocal()
    try:
        inserted = 0
        for nim, nama, kelas, prodi in DATA:
            exists = db.query(Mahasiswa).filter(Mahasiswa.nim == nim).first()
            if exists:
                continue
            m = Mahasiswa(nim=nim, nama=nama, kelas=kelas, prodi=prodi)
            db.add(m)
            inserted += 1
        db.commit()
        total = db.query(Mahasiswa).count()
        print(f"Inserted {inserted} new mahasiswa. Total rows now: {total}")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
