#!/bin/bash
# Setup script untuk Linux/Mac

echo "========================================="
echo "AbsenIN API - Setup Script"
echo "========================================="
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python3 tidak ditemukan!"
    echo "Install Python3 terlebih dahulu"
    exit 1
fi

echo "[1/6] Membuat virtual environment..."
python3 -m venv .venv
echo "✓ Virtual environment dibuat"

echo ""
echo "[2/6] Mengaktifkan virtual environment..."
source .venv/bin/activate
echo "✓ Virtual environment aktif"

echo ""
echo "[3/6] Upgrade pip..."
python -m pip install --upgrade pip
echo "✓ Pip upgraded"

echo ""
echo "[4/6] Install dependencies..."
pip install -r requirements.txt
echo "✓ Dependencies terinstall"

echo ""
echo "[5/6] Setup environment file..."
if [ ! -f .env ]; then
    cp .env.example .env
    echo "✓ File .env dibuat dari .env.example"
    echo ""
    echo "PENTING: Edit file .env dan sesuaikan konfigurasi database!"
else
    echo "✓ File .env sudah ada"
fi

echo ""
echo "[6/6] Membuat direktori logs..."
mkdir -p logs
echo "✓ Direktori logs dibuat"

echo ""
echo "========================================="
echo "Setup selesai!"
echo "========================================="
echo ""
echo "Langkah selanjutnya:"
echo "1. Edit file .env (sesuaikan DATABASE_URL)"
echo "2. Buat database: CREATE DATABASE absenin;"
echo "3. Jalankan migration: python -m alembic upgrade head"
echo "4. Jalankan seeder: python -m app.seed"
echo "5. Jalankan server: python -m uvicorn app.main:app --host 0.0.0.0 --port 8000"
echo ""
echo "Atau gunakan: ./start.sh"
echo ""
