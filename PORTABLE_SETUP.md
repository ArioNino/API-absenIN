# Panduan Portable Setup - API-absenIN

Panduan ini menjelaskan cara membuat project yang bisa dipindah-pindah device tanpa masalah.

## 🎯 Tujuan

Membuat project yang:
- ✅ Bisa di-clone di device manapun
- ✅ Tidak bergantung pada path absolut
- ✅ Setup otomatis dengan satu command
- ✅ Tidak perlu konfigurasi manual yang rumit

## 📦 Apa yang Harus Di-commit ke Git?

### ✅ COMMIT (Masuk ke Git)
```
✓ Source code (app/, alembic/)
✓ Configuration files (.env.example, alembic.ini)
✓ Dependencies list (requirements.txt)
✓ Documentation (README.md, dll)
✓ Helper scripts (setup.bat, run_*.bat)
✓ Migration files (alembic/versions/*.py)
```

### ❌ JANGAN COMMIT (Ada di .gitignore)
```
✗ Virtual environment (venv/)
✗ Environment variables (.env)
✗ Python cache (__pycache__/)
✗ IDE settings (.vscode/, .idea/)
✗ Database files (*.db, *.sqlite3)
✗ Log files (*.log)
```

## 🔄 Workflow: Pindah Device

### Device Lama (Sebelum Push)
```bash
# 1. Pastikan semua perubahan sudah di-commit
git status

# 2. Commit perubahan
git add .
git commit -m "Update features"

# 3. Push ke repository
git push origin main
```

### Device Baru (Setelah Clone)
```bash
# 1. Clone repository
git clone <repository-url>
cd API-absenIN

# 2. Jalankan setup (otomatis buat venv baru)
setup.bat

# 3. Edit .env sesuai konfigurasi lokal
notepad .env

# 4. Buat database
mysql -u root -p
CREATE DATABASE absenin;

# 5. Jalankan migration
run_migration.bat

# 6. (Opsional) Seed data
run_seed.bat

# 7. Jalankan server
run_server.bat
```

## 🛠️ Kenapa Virtual Environment Tidak Portable?

Virtual environment (venv) berisi:
- Path absolut ke Python interpreter
- Binary files yang spesifik untuk OS
- Symlinks yang terikat ke lokasi tertentu

Contoh path di venv:
```
venv/Scripts/python.exe
venv/pyvenv.cfg  # Berisi: home = C:\Users\UserLama\AppData\Local\Programs\Python
```

Jika folder dipindah atau di-clone, path ini menjadi invalid.

## ✅ Solusi: Setup Script

Script `setup.bat` akan:
1. Hapus venv lama (jika ada)
2. Buat venv baru di lokasi saat ini
3. Install semua dependencies dari requirements.txt
4. Copy .env.example ke .env (jika belum ada)

Dengan ini, setiap device akan punya venv sendiri yang sesuai dengan path lokalnya.

## 📝 Best Practices

### 1. Selalu Gunakan Relative Path
```python
# ❌ SALAH - Absolute path
DATABASE_URL = "C:/Users/Ario/project/database.db"

# ✅ BENAR - Relative atau dari environment
DATABASE_URL = os.getenv("DATABASE_URL")
```

### 2. Gunakan Environment Variables
```python
# ❌ SALAH - Hardcoded
SECRET_KEY = "my-secret-key-123"

# ✅ BENAR - Dari .env
SECRET_KEY = os.getenv("SECRET_KEY")
```

### 3. Dokumentasikan Dependencies
```bash
# Update requirements.txt setelah install package baru
pip freeze > requirements.txt
```

### 4. Gunakan Helper Scripts
```bash
# ❌ SALAH - Command panjang yang harus diingat
venv\Scripts\activate && python -m alembic upgrade head

# ✅ BENAR - Script helper
run_migration.bat
```

## 🔍 Troubleshooting

### Problem: "Unable to create process using venv\Scripts\python.exe"

**Penyebab**: Venv dibuat di device lain

**Solusi**:
```bash
# Hapus venv lama
rmdir /s /q venv

# Buat venv baru
setup.bat
```

### Problem: "Module not found"

**Penyebab**: Dependencies belum terinstall di venv baru

**Solusi**:
```bash
# Aktifkan venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Problem: "Database connection failed"

**Penyebab**: .env masih berisi konfigurasi device lama

**Solusi**:
```bash
# Edit .env
notepad .env

# Sesuaikan dengan konfigurasi lokal
DATABASE_URL=mysql+pymysql://root:PASSWORD_LOKAL@localhost/absenin
```

## 📚 Struktur File Project

```
API-absenIN/
├── app/                    # Source code (COMMIT)
├── alembic/                # Migrations (COMMIT)
├── venv/                   # Virtual env (JANGAN COMMIT)
├── .env                    # Config lokal (JANGAN COMMIT)
├── .env.example            # Template config (COMMIT)
├── requirements.txt        # Dependencies (COMMIT)
├── setup.bat               # Setup script (COMMIT)
├── run_*.bat               # Helper scripts (COMMIT)
├── README.md               # Dokumentasi (COMMIT)
└── .gitignore              # Git ignore rules (COMMIT)
```

## 🎓 Tips untuk Tim Development

### Untuk Developer Baru
1. Clone repository
2. Jalankan `setup.bat`
3. Baca `MULAI_DISINI.txt`
4. Ikuti instruksi di `QUICKSTART.md`

### Untuk Developer yang Update Code
1. `git pull` untuk update code
2. Cek `requirements.txt` ada perubahan?
   - Jika ya: `pip install -r requirements.txt`
3. Cek ada migration baru?
   - Jika ya: `run_migration.bat`
4. Jalankan server: `run_server.bat`

### Untuk Developer yang Pindah Device
1. Push semua perubahan dari device lama
2. Clone di device baru
3. Jalankan `setup.bat`
4. Edit `.env` sesuai konfigurasi lokal
5. Jalankan `run_migration.bat`

## 🚀 Automation Tips

### Pre-commit Hook (Opsional)
Buat file `.git/hooks/pre-commit`:
```bash
#!/bin/sh
# Cek apakah ada file yang tidak seharusnya di-commit

if git diff --cached --name-only | grep -q "^venv/"; then
    echo "ERROR: Jangan commit folder venv/"
    exit 1
fi

if git diff --cached --name-only | grep -q "^\.env$"; then
    echo "ERROR: Jangan commit file .env"
    exit 1
fi
```

### Post-merge Hook (Opsional)
Buat file `.git/hooks/post-merge`:
```bash
#!/bin/sh
# Auto install dependencies setelah pull

if [ -f requirements.txt ]; then
    echo "Checking for new dependencies..."
    pip install -r requirements.txt
fi
```

## 📖 Referensi

- [Python venv documentation](https://docs.python.org/3/library/venv.html)
- [Git .gitignore patterns](https://git-scm.com/docs/gitignore)
- [12 Factor App - Config](https://12factor.net/config)

## ✨ Kesimpulan

Dengan setup yang benar:
- ✅ Project bisa di-clone di device manapun
- ✅ Setup hanya butuh 1 command: `setup.bat`
- ✅ Tidak ada dependency pada path absolut
- ✅ Setiap developer punya environment sendiri
- ✅ Konfigurasi lokal tidak mengganggu developer lain

**Ingat**: Virtual environment itu seperti "workspace lokal" - setiap device harus punya sendiri!
