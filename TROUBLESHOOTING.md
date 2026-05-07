# Troubleshooting Guide - API-absenIN

Panduan mengatasi masalah umum yang mungkin terjadi.

## 🔴 Error: Permission Denied (PENTING!)

### Error: "[Errno 13] Permission denied: venv\Scripts\python.exe"

**Penyebab**: Ada proses yang masih menggunakan file di folder venv.

**Solusi Cepat**:
1. Tutup SEMUA Command Prompt / PowerShell
2. Tutup VS Code / IDE
3. Buka Task Manager (Ctrl+Shift+Esc)
4. End Task semua proses `python.exe`
5. Tunggu 10 detik
6. Jalankan `setup.bat` lagi

**Solusi Alternatif**:
```bash
# Gunakan script helper
delete_venv.bat

# Atau hapus manual di File Explorer
# Lalu jalankan setup.bat
```

**Lihat panduan lengkap**: `PERMISSION_DENIED_FIX.md`

---

## 🔴 Error: Virtual Environment

### Error: "Virtual environment tidak ditemukan"
```
ERROR: Virtual environment tidak ditemukan!
Jalankan setup.bat terlebih dahulu.
```

**Penyebab**: Virtual environment belum dibuat atau terhapus.

**Solusi**:
```bash
setup.bat
```

### Error: "Unable to create process using venv\Scripts\python.exe"
```
Fatal error in launcher: Unable to create process using 
'"C:\Users\...\venv\Scripts\python.exe"': The system cannot find the file specified.
```

**Penyebab**: Virtual environment dibuat di device lain atau path berubah.

**Solusi**:
1. Hapus folder `venv/`
2. Jalankan `setup.bat` untuk membuat venv baru

```bash
# Hapus venv lama
rmdir /s /q venv

# Buat venv baru
setup.bat
```

## 🔴 Error: Database

### Error: "Can't connect to MySQL server"
```
sqlalchemy.exc.OperationalError: (pymysql.err.OperationalError) 
(2003, "Can't connect to MySQL server on 'localhost'")
```

**Penyebab**: MySQL server tidak berjalan atau konfigurasi salah.

**Solusi**:
1. Pastikan MySQL server berjalan
2. Cek konfigurasi di `.env`:
```env
DATABASE_URL=mysql+pymysql://root:PASSWORD@localhost/absenin
```
3. Test koneksi MySQL:
```bash
mysql -u root -p
```

### Error: "Unknown database 'absenin'"
```
sqlalchemy.exc.OperationalError: (pymysql.err.OperationalError) 
(1049, "Unknown database 'absenin'")
```

**Penyebab**: Database belum dibuat.

**Solusi**:
```sql
-- Buka MySQL
mysql -u root -p

-- Buat database
CREATE DATABASE absenin;

-- Cek database
SHOW DATABASES;
```

### Error: "Access denied for user"
```
sqlalchemy.exc.OperationalError: (pymysql.err.OperationalError) 
(1045, "Access denied for user 'root'@'localhost'")
```

**Penyebab**: Password MySQL salah di `.env`.

**Solusi**:
1. Cek password MySQL Anda
2. Update file `.env`:
```env
DATABASE_URL=mysql+pymysql://root:PASSWORD_YANG_BENAR@localhost/absenin
```

## 🔴 Error: Migration

### Error: "Target database is not up to date"
```
FAILED: Target database is not up to date.
```

**Solusi**:
```bash
run_migration.bat
```

### Error: "Can't locate revision identified by"
```
Can't locate revision identified by 'xxxxx'
```

**Penyebab**: Migration history tidak sinkron.

**Solusi**:
```bash
# Cek current revision
python -m alembic current

# Downgrade ke base
python -m alembic downgrade base

# Upgrade ke head
run_migration.bat
```

## 🔴 Error: Dependencies

### Error: "No module named 'fastapi'"
```
ModuleNotFoundError: No module named 'fastapi'
```

**Penyebab**: Dependencies belum terinstall.

**Solusi**:
```bash
# Aktifkan venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Error: "No module named 'pydantic_settings'"
```
ModuleNotFoundError: No module named 'pydantic_settings'
```

**Penyebab**: Dependency baru belum terinstall.

**Solusi**:
```bash
pip install pydantic-settings
# atau
pip install -r requirements.txt --upgrade
```

## 🔴 Error: Server

### Error: "Address already in use"
```
OSError: [Errno 48] Address already in use
```

**Penyebab**: Port 8000 sudah digunakan.

**Solusi**:
1. Hentikan server yang berjalan (Ctrl+C)
2. Atau gunakan port lain:
```bash
python -m uvicorn app.main:app --reload --port 8001
```

### Error: "Application startup failed"
```
ERROR:    Application startup failed. Exiting.
```

**Penyebab**: Error di kode atau konfigurasi.

**Solusi**:
1. Cek error message di atas
2. Pastikan `.env` sudah ada dan benar
3. Pastikan database bisa diakses
4. Cek log error untuk detail

## 🔴 Error: Import

### Error: "cannot import name 'get_settings'"
```
ImportError: cannot import name 'get_settings' from 'app.config'
```

**Penyebab**: File `app/config.py` tidak ada atau rusak.

**Solusi**:
1. Pastikan file `app/config.py` ada
2. Pastikan isi file benar
3. Restart server

## 🔴 Error: Authentication

### Error: "Token tidak valid atau sudah kadaluarsa"
```
{"detail": "Token tidak valid atau sudah kadaluarsa"}
```

**Penyebab**: Token JWT expired atau salah.

**Solusi**:
1. Login ulang untuk mendapatkan token baru
2. Pastikan menggunakan format: `Bearer <token>`

### Error: "Email tidak ditemukan"
```
{"detail": "Email tidak ditemukan"}
```

**Penyebab**: User belum ada di database.

**Solusi**:
```bash
# Jalankan seeder untuk membuat user default
run_seed.bat
```

## 🔴 Error: File .env

### Error: "Field required [type=missing]"
```
pydantic_core._pydantic_core.ValidationError: 1 validation error for Settings
DATABASE_URL
  Field required [type=missing, input_value={}, input_type=dict]
```

**Penyebab**: File `.env` tidak ada atau tidak lengkap.

**Solusi**:
1. Copy dari template:
```bash
copy .env.example .env
```
2. Edit `.env` dan isi semua field yang required

## 📞 Masih Ada Masalah?

Jika masalah masih berlanjut:

1. **Cek log error** dengan teliti
2. **Pastikan semua prerequisites** terinstall:
   - Python 3.8+
   - MySQL Server
   - pip
3. **Jalankan setup ulang**:
```bash
# Hapus venv
rmdir /s /q venv

# Setup ulang
setup.bat
```
4. **Cek dokumentasi** di `README.md`
5. **Buat issue** di repository dengan:
   - Error message lengkap
   - Langkah yang sudah dicoba
   - Screenshot jika perlu

## 💡 Tips Debugging

### Cek Status Komponen

```bash
# Cek Python version
python --version

# Cek pip version
pip --version

# Cek MySQL status
mysql --version

# Cek installed packages
pip list

# Cek alembic current revision
python -m alembic current

# Test database connection
python -c "from app.database import engine; print(engine.connect())"
```

### Mode Verbose

Jalankan command dengan flag verbose untuk detail error:

```bash
# Migration dengan verbose
python -m alembic upgrade head --verbose

# Server dengan log level debug
python -m uvicorn app.main:app --reload --log-level debug
```
