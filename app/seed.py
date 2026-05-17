"""Main seeder command to run all seeders."""
from app.seeders.user_seeder import UserSeeder
from app.seeders.dosen_seeder import DosenSeeder
from app.seeders.matakuliah_seeder import MataKuliahSeeder
from app.seeders.kelas_seeder import KelasSeeder
from app.seeders.mahasiswa_seeder import MahasiswaSeeder
from app.seeders.kelas_mahasiswa_seeder import KelasMahasiswaSeeder

def run_all_seeders():
    """Run all seeders in order."""
    seeders = [
        ("User", UserSeeder),
        ("Dosen", DosenSeeder),
        ("MataKuliah", MataKuliahSeeder),
        ("Kelas", KelasSeeder),
        ("Mahasiswa", MahasiswaSeeder),
        ("KelasMahasiswa", KelasMahasiswaSeeder)
    ]

    print("=" * 60)
    print("Running Database Seeders")
    print("=" * 60)

    for name, seeder_class in seeders:
        try:
            print(f"\n[{name}] Seeding...")
            seeder = seeder_class()
            seeder.seed()
            print(f"[{name}] {seeder.report()}")
            seeder.close()
        except Exception as e:
            print(f"[{name}] ERROR: {str(e)}")

    print("\n" + "=" * 60)
    print("Seeding completed!")
    print("=" * 60)


if __name__ == "__main__":
    run_all_seeders()

