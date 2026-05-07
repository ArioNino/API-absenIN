@echo off
REM Script untuk menjalankan database seeder

REM Change to script directory
cd /d "%~dp0"

echo ========================================
echo Running Database Seeders
echo ========================================
echo.
echo Working directory: %CD%
echo.

REM Activate virtual environment
if not exist venv\Scripts\activate.bat (
    echo ERROR: Virtual environment tidak ditemukan!
    echo Jalankan setup.bat terlebih dahulu.
    pause
    exit /b 1
)

call venv\Scripts\activate.bat

echo Menjalankan seeders...
python -m app.seed

if errorlevel 1 (
    echo.
    echo ERROR: Seeding gagal!
    echo.
    echo Pastikan:
    echo 1. Database sudah dibuat
    echo 2. Migrations sudah dijalankan
    echo 3. Konfigurasi di .env sudah benar
    echo.
    echo Lihat error message di atas untuk detail.
    pause
    exit /b 1
)

echo.
echo ========================================
echo Seeding berhasil!
echo ========================================
echo.
echo Default users:
echo - Email: admin@absenin.local, Password: admin123
echo - Email: dosen@absenin.local, Password: dosen123
echo.
pause
