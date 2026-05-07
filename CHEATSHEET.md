# 📋 Command Cheatsheet - API-absenIN

Quick reference untuk command yang sering digunakan.

## 🚀 Setup & Installation

```bash
# Setup pertama kali (buat venv, install deps)
setup.bat

# Install dependency baru
venv\Scripts\activate
pip install <package-name>
pip freeze > requirements.txt

# Update dependencies
pip install -r requirements.txt --upgrade
```

## 🗄️ Database & Migrations

```bash
# Jalankan migrations
run_migration.bat

# Buat migration baru
create_migration.bat "deskripsi_perubahan"

# Rollback migration
python -m alembic downgrade -1

# Cek current revision
python -m alembic current

# Lihat history migrations
python -m alembic history

# Seed database
run_seed.bat
```

## 🖥️ Server

```bash
# Jalankan server (development)
run_server.bat

# Jalankan server manual
venv\Scripts\activate
python -m uvicorn app.main:app --reload

# Jalankan di port lain
python -m uvicorn app.main:app --reload --port 8001

# Jalankan dengan host 0.0.0.0 (akses dari network)
python -m uvicorn app.main:app --reload --host 0.0.0.0
```

## 🧪 Testing API

```bash
# Akses dokumentasi interaktif
http://localhost:8000/docs

# Test endpoint dengan curl
curl -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d "{\"email\":\"dosen@absenin.local\",\"password\":\"dosen123\"}"

# Test dengan token
curl -X GET http://localhost:8000/mahasiswa/ \
  -H "Authorization: Bearer <your-token>"
```

## 🔍 Debugging

```bash
# Cek Python version
python --version

# Cek installed packages
pip list

# Cek package tertentu
pip show fastapi

# Test database connection
python -c "from app.database import engine; print(engine.connect())"

# Test import module
python -c "from app.config import get_settings; print(get_settings())"

# Jalankan Python shell dengan context
python
>>> from app.database import SessionLocal
>>> from app.models.user import User
>>> db = SessionLocal()
>>> users = db.query(User).all()
>>> print(users)
```

## 📦 Virtual Environment

```bash
# Aktifkan venv
venv\Scripts\activate

# Deaktifkan venv
deactivate

# Hapus venv
rmdir /s /q venv

# Buat venv baru
python -m venv venv
```

## 🗃️ MySQL Commands

```bash
# Login ke MySQL
mysql -u root -p

# Buat database
CREATE DATABASE absenin;

# Lihat databases
SHOW DATABASES;

# Gunakan database
USE absenin;

# Lihat tables
SHOW TABLES;

# Lihat struktur table
DESCRIBE mahasiswa;

# Query data
SELECT * FROM users;

# Drop database (HATI-HATI!)
DROP DATABASE absenin;
```

## 📝 Git Commands

```bash
# Clone repository
git clone <repository-url>

# Cek status
git status

# Add files
git add .

# Commit
git commit -m "Deskripsi perubahan"

# Push
git push origin main

# Pull
git pull

# Lihat log
git log --oneline

# Buat branch baru
git checkout -b feature/nama-fitur

# Pindah branch
git checkout main

# Merge branch
git merge feature/nama-fitur
```

## 🔧 Alembic Advanced

```bash
# Generate migration (manual)
python -m alembic revision -m "deskripsi"

# Generate migration (auto-detect changes)
python -m alembic revision --autogenerate -m "deskripsi"

# Upgrade ke revision tertentu
python -m alembic upgrade <revision_id>

# Downgrade ke revision tertentu
python -m alembic downgrade <revision_id>

# Upgrade ke head
python -m alembic upgrade head

# Downgrade ke base (hapus semua)
python -m alembic downgrade base

# Show current revision
python -m alembic current

# Show history
python -m alembic history --verbose

# Show SQL yang akan dijalankan (dry-run)
python -m alembic upgrade head --sql
```

## 🐍 Python Shell Commands

```python
# Import models
from app.models.user import User
from app.models.mahasiswa import Mahasiswa
from app.database import SessionLocal

# Create session
db = SessionLocal()

# Query all
users = db.query(User).all()

# Query with filter
user = db.query(User).filter(User.email == "dosen@absenin.local").first()

# Create new record
new_user = User(email="test@test.com", name="Test User", password="hashed")
db.add(new_user)
db.commit()

# Update record
user.name = "New Name"
db.commit()

# Delete record
db.delete(user)
db.commit()

# Close session
db.close()
```

## 📊 Useful One-liners

```bash
# Count lines of code
find app -name "*.py" | xargs wc -l

# Find TODO comments
grep -r "TODO" app/

# Find FIXME comments
grep -r "FIXME" app/

# List all routes
python -c "from app.main import app; print([route.path for route in app.routes])"

# Check for syntax errors
python -m py_compile app/**/*.py

# Format code with black (if installed)
black app/

# Sort imports with isort (if installed)
isort app/
```

## 🔐 Security

```bash
# Generate secret key
python -c "import secrets; print(secrets.token_urlsafe(32))"

# Hash password
python -c "from app.utils.security import hash_password; print(hash_password('mypassword'))"

# Verify password
python -c "from app.utils.security import verify_password; print(verify_password('plain', 'hashed'))"
```

## 📦 Package Management

```bash
# Install from requirements.txt
pip install -r requirements.txt

# Install specific version
pip install fastapi==0.104.1

# Uninstall package
pip uninstall <package-name>

# Update pip
python -m pip install --upgrade pip

# Show outdated packages
pip list --outdated

# Update package
pip install --upgrade <package-name>
```

## 🎯 Quick Fixes

```bash
# Fix: Module not found
pip install -r requirements.txt

# Fix: Database connection error
# Edit .env dan cek konfigurasi

# Fix: Migration error
python -m alembic downgrade -1
python -m alembic upgrade head

# Fix: Port already in use
# Hentikan server yang berjalan atau gunakan port lain
python -m uvicorn app.main:app --reload --port 8001

# Fix: Virtual environment error
rmdir /s /q venv
setup.bat
```

## 📱 API Endpoints Quick Reference

```
POST   /auth/login              - Login
GET    /mahasiswa/              - List mahasiswa
GET    /mahasiswa/{id}          - Get mahasiswa by ID
GET    /mahasiswa/nim/{nim}     - Get mahasiswa by NIM
POST   /mahasiswa/              - Create mahasiswa
PUT    /mahasiswa/{id}          - Update mahasiswa
DELETE /mahasiswa/{id}          - Delete mahasiswa
GET    /kehadiran/              - List kehadiran
GET    /kehadiran/bap/{id}      - Get kehadiran by BAP
GET    /kehadiran/mahasiswa/{id} - Get kehadiran by mahasiswa
POST   /kehadiran/              - Create kehadiran
PUT    /kehadiran/{id}          - Update kehadiran
DELETE /kehadiran/{id}          - Delete kehadiran
GET    /berita-acara/           - List berita acara
GET    /berita-acara/dosen/{id} - Get BAP by dosen
GET    /berita-acara/kelas/{id} - Get BAP by kelas
POST   /berita-acara/           - Create BAP
PUT    /berita-acara/{id}       - Update BAP
DELETE /berita-acara/{id}       - Delete BAP
```

## 💡 Tips

- Selalu aktifkan venv sebelum menjalankan command Python
- Commit perubahan secara berkala
- Buat migration setelah mengubah models
- Test API di /docs sebelum integrate ke frontend
- Backup database sebelum menjalankan migration di production
- Gunakan .env untuk konfigurasi, jangan hardcode
- Baca error message dengan teliti
- Cek TROUBLESHOOTING.md jika ada masalah

---

**Simpan file ini untuk referensi cepat!** 📌
