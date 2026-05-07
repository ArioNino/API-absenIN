# AbsenIN API - Quick Start

## ✅ Setup Selesai!

Project sudah siap digunakan dengan data dummy di memory.

### 🚀 Menjalankan Server

```bash
start.bat
```

Atau manual:
```bash
.venv\Scripts\python.exe -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

### 📍 Endpoints

Server berjalan di: **http://127.0.0.1:8000**

#### Dokumentasi
- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

#### API Endpoints

| Method | Endpoint | Deskripsi |
|--------|----------|-----------|
| GET | `/` | Hello World + info API |
| GET | `/health` | Health check |
| GET | `/mahasiswa` | List semua mahasiswa |
| GET | `/mahasiswa/{id}` | Get mahasiswa by ID |
| GET | `/mahasiswa/nim/{nim}` | Get mahasiswa by NIM |
| GET | `/kehadiran` | List semua kehadiran |
| GET | `/kehadiran/{id}` | Get kehadiran by ID |
| GET | `/stats` | Statistik kehadiran |

### 📊 Data Dummy

#### Mahasiswa (5 data)
- AZZAHRA NABILA CHAIRONA (J0403231006)
- KEVIN FARHAN HERNANDEZ (J0403231019)
- PUTI AISYAH LAILATULRAHMI (J0403231031)
- ARIO ELNINO (J0403231035)
- Nika Rani Nur Shafa Lubis (J0403231041)

#### Kehadiran (5 data)
- 3 Hadir
- 1 Izin
- 1 Alpha

### 🧪 Test API

#### 1. Hello World
```bash
curl http://127.0.0.1:8000/
```

Response:
```json
{
  "message": "Hello World from AbsenIN API!",
  "status": "running",
  "version": "1.0.0"
}
```

#### 2. Get All Mahasiswa
```bash
curl http://127.0.0.1:8000/mahasiswa
```

#### 3. Get Mahasiswa by NIM
```bash
curl http://127.0.0.1:8000/mahasiswa/nim/J0403231006
```

#### 4. Get Statistics
```bash
curl http://127.0.0.1:8000/stats
```

### 📝 Catatan

- ✅ Virtual environment: `.venv`
- ✅ Dependencies: Sudah terinstall
- ✅ Data: Dummy data di memory (tidak perlu database)
- ✅ CORS: Enabled untuk development
- ✅ Auto-reload: Enabled (perubahan code otomatis reload)

### 🔄 Next Steps (Opsional)

Jika ingin menggunakan database MySQL:

1. Install dan jalankan MySQL server
2. Buat database: `CREATE DATABASE absenin;`
3. Edit `.env` sesuai konfigurasi MySQL Anda
4. Jalankan migrations: `.venv\Scripts\python.exe -m alembic upgrade head`
5. Jalankan seeders: `.venv\Scripts\python.exe -m app.seed`
6. Update `app/main.py` untuk menggunakan database

### 🎉 Selesai!

API sudah berjalan dengan data dummy. Akses http://127.0.0.1:8000/docs untuk mencoba semua endpoint.
