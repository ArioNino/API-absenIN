from app.database import SessionLocal
from app.models.mahasiswa import Mahasiswa

DATA = [
    ("J0403231006", "AZZAHRA NABILA CHAIRONA"),
    ("J0403231019", "KEVIN FARHAN HERNANDEZ"),
    ("J0403231031", "PUTI AISYAH LAILATULRAHMI"),
    ("J0403231035", "ARIO ELNINO"),
    ("J0403231041", "Nika Rani Nur Shafa Lubis"),
    ("J0403231056", "Khinanti Angelita Puteri"),
    ("J0403231061", "MUHAMMAD RAIHAN ZALDIPUTRA"),
    ("J0403231094", "Faliana Alifia"),
    ("J0403231132", "Jonathan"),
    ("J0403231166", "GHANIYY FATTAH RAMADHAN"),
    ("J0405231059", "MUHAMMAD FAKHRI HAKIM"),
    ("J0410231051", "Sarah Nahdiyatul Hasanah"),
    ("J0410231092", "Achmad Fauzan Wicaksono"),
    ("J0410231105", "Arta Novriana Napitupulu"),
    ("J0410231121", "ALYA YUNISA AULIAWATI"),
    ("J0410231154", "Dara Dynanti"),
]


def seed():
    db = SessionLocal()
    try:
        inserted = 0
        for nim, nama in DATA:
            exists = db.query(Mahasiswa).filter(Mahasiswa.nim == nim).first()
            if exists:
                continue
            m = Mahasiswa(nim=nim, nama=nama)
            db.add(m)
            inserted += 1
        db.commit()
        total = db.query(Mahasiswa).count()
        print(f"Inserted {inserted} new mahasiswa. Total rows now: {total}")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
