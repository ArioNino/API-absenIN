# AbsenIN API

API backend untuk sistem manajemen absensi mahasiswa berbasis FastAPI.

## 🚀 Quick Start

**Pertama kali setup?** Baca file `MULAI_DISINI.txt` atau ikuti [Quick Start Guide](QUICKSTART.md)

```bash
# 1. Setup (otomatis buat venv & install dependencies)
setup.bat

# 2. Edit konfigurasi database
notepad .env

# 3. Buat database
CREATE DATABASE absenin;

# 4. Jalankan migration
run_migration.bat

# 5. Jalankan server
run_server.bat
```

**Selesai!** Akses http://localhost:8000/docs

## 📚 Dokumentasi

| Dokumen | Deskripsi |
|---------|-----------|
| [MULAI_DISINI.txt](MULAI_DISINI.txt) | 📖 Baca ini pertama kali! |
| [QUICKSTART.md](QUICKSTART.md) | ⚡ Panduan cepat 5 menit |
| [CHEATSHEET.md](CHEATSHEET.md) | 📋 Command reference |
| [TROUBLESHOOTING.md](TROUBLESHOOTING.md) | 🔧 Solusi masalah umum |
| [PORTABLE_SETUP.md](PORTABLE_SETUP.md) | 📦 Penjelasan portable setup |
| [SOLUSI_PORTABLE.md](SOLUSI_PORTABLE.md) | ✨ Summary solusi portable |
| [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md) | 📝 Summary implementasi |

## Fitur

- ✅ Autentikasi JWT
- ✅ Manajemen data mahasiswa
- ✅ Pencatatan kehadiran
- ✅ Berita Acara Perkuliahan (BAP)
- ✅ Manajemen kelas dan mata kuliah
- ✅ Database migrations dengan Alembic
- ✅ Dokumentasi API otomatis (Swagger/OpenAPI)

## Tech Stack

- **Framework**: FastAPI
- **Database**: MySQL
- **ORM**: SQLAlchemy
- **Migrations**: Alembic
- **Authentication**: JWT (python-jose)
- **Password Hashing**: Bcrypt (passlib)

## Instalasi

### Prerequisites

- Python 3.8+
- MySQL Server
- pip

### Setup Otomatis (Windows) - RECOMMENDED ⭐

Untuk setup yang mudah dan portable (bisa pindah device), gunakan script otomatis:

1. **Clone repository**:
```bash
git clone <repository-url>
cd API-absenIN
```

2. **Jalankan setup**:
```bash
setup.bat
```

Script ini akan:
- Membuat virtual environment baru
- Install semua dependencies
- Membuat file .env dari template

3. **Edit file `.env`** dan sesuaikan konfigurasi database:
```env
DATABASE_URL=mysql+pymysql://root:password@localhost/absenin
SECRET_KEY=your-secret-key-here
```

4. **Buat database MySQL**:
```sql
CREATE DATABASE absenin;
```

5. **Jalankan migrations**:
```bash
run_migration.bat
```

6. **(Opsional) Seed database dengan data contoh**:
```bash
run_seed.bat
```

7. **Jalankan server**:
```bash
run_server.bat
```

### Setup Manual (Linux/Mac/Windows)

1. Clone repository:
```bash
git clone <repository-url>
cd API-absenIN
```

2. Buat virtual environment:
```bash
python -m venv venv
```

3. Aktifkan virtual environment:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Copy file `.env.example` ke `.env` dan sesuaikan konfigurasi:
```bash
# Windows
copy .env.example .env

# Linux/Mac
cp .env.example .env
```

Edit `.env`:
```env
DATABASE_URL=mysql+pymysql://root:password@localhost/absenin
SECRET_KEY=your-secret-key-here
```

6. Buat database MySQL:
```sql
CREATE DATABASE absenin;
```

7. Jalankan migrations:
```bash
# Windows (gunakan python -m)
python -m alembic upgrade head

# Linux/Mac
alembic upgrade head
```

8. (Opsional) Seed database dengan data contoh:
```bash
python -m app.seed
```

## Menjalankan Server

### Menggunakan Script (Windows)
```bash
run_server.bat
```

### Manual
Development mode:
```bash
# Aktifkan virtual environment terlebih dahulu
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate

# Jalankan server
uvicorn app.main:app --reload
```

Server akan berjalan di `http://localhost:8000`

## Script Helper (Windows)

Project ini dilengkapi dengan script helper untuk memudahkan development:

| Script | Fungsi |
|--------|--------|
| `setup.bat` | Setup awal project (install dependencies, buat venv) |
| `run_migration.bat` | Jalankan database migrations |
| `create_migration.bat "nama"` | Buat migration baru |
| `run_seed.bat` | Seed database dengan data contoh |
| `run_server.bat` | Jalankan development server |

### Contoh Penggunaan

```bash
# Setup pertama kali
setup.bat

# Buat migration baru
create_migration.bat "add_new_field"

# Jalankan migration
run_migration.bat

# Seed database
run_seed.bat

# Jalankan server
run_server.bat
```

## Pindah Device / Clone Baru

Jika Anda clone project di device baru atau pindah folder:

1. **Jangan copy folder `venv/`** (sudah ada di .gitignore)
2. Jalankan `setup.bat` untuk membuat virtual environment baru
3. Edit `.env` sesuai konfigurasi database lokal Anda
4. Jalankan `run_migration.bat`
5. (Opsional) Jalankan `run_seed.bat`
6. Jalankan `run_server.bat`

**Catatan**: Virtual environment bersifat lokal dan tidak portable. Selalu buat ulang dengan `setup.bat` di device baru.

## Dokumentasi API

Setelah server berjalan, akses dokumentasi interaktif di:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Struktur Database

### Tabel Utama

- `users` - Data pengguna (autentikasi)
- `dosen` - Data dosen
- `mahasiswa` - Data mahasiswa
- `mata_kuliah` - Data mata kuliah
- `kelas` - Data kelas perkuliahan
- `berita_acara_perkuliahan` - Catatan sesi perkuliahan
- `kehadiran` - Catatan kehadiran mahasiswa
- `kelas_mahasiswa` - Relasi mahasiswa-kelas
- `kelas_dosen` - Relasi dosen-kelas

## Endpoint API

### Authentication
- `POST /auth/login` - Login dan dapatkan JWT token

### Mahasiswa
- `GET /mahasiswa/` - List semua mahasiswa
- `GET /mahasiswa/{id}` - Detail mahasiswa
- `GET /mahasiswa/nim/{nim}` - Cari mahasiswa by NIM
- `POST /mahasiswa/` - Tambah mahasiswa baru
- `PUT /mahasiswa/{id}` - Update mahasiswa
- `DELETE /mahasiswa/{id}` - Hapus mahasiswa

### Kehadiran
- `GET /kehadiran/` - List semua kehadiran
- `GET /kehadiran/bap/{bap_id}` - Kehadiran per BAP
- `GET /kehadiran/mahasiswa/{id}` - Kehadiran per mahasiswa
- `POST /kehadiran/` - Catat kehadiran
- `PUT /kehadiran/{id}` - Update kehadiran
- `DELETE /kehadiran/{id}` - Hapus kehadiran

### Berita Acara Perkuliahan
- `GET /berita-acara/` - List semua BAP
- `GET /berita-acara/dosen/{id}` - BAP per dosen
- `GET /berita-acara/kelas/{id}` - BAP per kelas
- `POST /berita-acara/` - Buat BAP baru
- `PUT /berita-acara/{id}` - Update BAP
- `DELETE /berita-acara/{id}` - Hapus BAP

## Autentikasi

Semua endpoint (kecuali `/auth/login`) memerlukan JWT token.

### Cara Menggunakan

1. Login untuk mendapatkan token:
```bash
curl -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "dosen@absenin.local", "password": "dosen123"}'
```

2. Gunakan token di header request:
```bash
curl -X GET http://localhost:8000/mahasiswa/ \
  -H "Authorization: Bearer <your-token-here>"
```

## Default Users (Setelah Seeding)

- **Admin**: 
  - Email: `admin@absenin.local`
  - Password: `admin123`

- **Dosen**:
  - Email: `dosen@absenin.local`
  - Password: `dosen123`

## Development

### Membuat Migration Baru

```bash
# Windows (gunakan script)
create_migration.bat "description"

# Manual
python -m alembic revision --autogenerate -m "description"
```

### Menjalankan Migration

```bash
# Windows (gunakan script)
run_migration.bat

# Manual
python -m alembic upgrade head
```

### Rollback Migration

```bash
python -m alembic downgrade -1
```

## Struktur Project

```
API-absenIN/
├── alembic/              # Database migrations
│   └── versions/         # Migration files
├── app/
│   ├── models/           # SQLAlchemy models
│   ├── routes/           # API endpoints
│   ├── schemas/          # Pydantic schemas
│   ├── seeders/          # Database seeders
│   ├── utils/            # Utility functions
│   ├── config.py         # Configuration
│   ├── database.py       # Database setup
│   ├── main.py           # FastAPI app
│   └── seed.py           # Seeder runner
├── .env                  # Environment variables (not in git)
├── .env.example          # Example environment file
├── alembic.ini           # Alembic configuration
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Contributing

1. Fork repository
2. Buat branch baru (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

## License

[Specify your license here]

## Contact

[Your contact information]
