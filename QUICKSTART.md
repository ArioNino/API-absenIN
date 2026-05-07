# Quick Start Guide - API-absenIN

Panduan cepat untuk menjalankan project di device baru.

## 🚀 Setup Cepat (5 Menit)

### 1. Clone Project
```bash
git clone <repository-url>
cd API-absenIN
```

### 2. Jalankan Setup
```bash
setup.bat
```

### 3. Konfigurasi Database
Edit file `.env`:
```env
DATABASE_URL=mysql+pymysql://root:YOUR_PASSWORD@localhost/absenin
```

### 4. Buat Database
Buka MySQL dan jalankan:
```sql
CREATE DATABASE absenin;
```

### 5. Jalankan Migration
```bash
run_migration.bat
```

### 6. Seed Data (Opsional)
```bash
run_seed.bat
```

### 7. Jalankan Server
```bash
run_server.bat
```

## ✅ Selesai!

Server berjalan di: http://localhost:8000
Dokumentasi API: http://localhost:8000/docs

## 🔑 Default Login

Setelah seeding:
- **Dosen**: dosen@absenin.local / dosen123
- **Admin**: admin@absenin.local / admin123

## 🧪 Test API

1. Buka http://localhost:8000/docs
2. Klik endpoint `/auth/login`
3. Klik "Try it out"
4. Masukkan:
```json
{
  "email": "dosen@absenin.local",
  "password": "dosen123"
}
```
5. Klik "Execute"
6. Copy token dari response
7. Klik tombol "Authorize" di atas
8. Paste token (dengan prefix "Bearer ")
9. Sekarang Anda bisa test semua endpoint!

## ❓ Troubleshooting

### Error: Virtual environment tidak ditemukan
**Solusi**: Jalankan `setup.bat` terlebih dahulu

### Error: Database connection failed
**Solusi**: 
- Pastikan MySQL server berjalan
- Cek konfigurasi di file `.env`
- Pastikan database `absenin` sudah dibuat

### Error: Migration failed
**Solusi**:
- Pastikan database sudah dibuat
- Cek koneksi database di `.env`
- Jalankan ulang `run_migration.bat`

### Error: Module not found
**Solusi**: Jalankan ulang `setup.bat` untuk install dependencies

## 📝 Workflow Development

```bash
# 1. Buat perubahan di models
# Edit file di app/models/

# 2. Buat migration
create_migration.bat "deskripsi_perubahan"

# 3. Review migration
# Cek file di alembic/versions/

# 4. Jalankan migration
run_migration.bat

# 5. Test perubahan
run_server.bat
```

## 🔄 Pindah Device Baru

1. Clone project (jangan copy folder `venv/`)
2. Jalankan `setup.bat`
3. Edit `.env` sesuai konfigurasi lokal
4. Jalankan `run_migration.bat`
5. Jalankan `run_server.bat`

## 📚 Dokumentasi Lengkap

Lihat `README.md` untuk dokumentasi lengkap.
