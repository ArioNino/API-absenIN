@echo off
REM Script untuk menjalankan Alembic migrations

REM Change to script directory
cd /d "%~dp0"

echo ========================================
echo Running Database Migrations
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

REM Check if alembic is installed
python -c "import alembic" 2>nul
if errorlevel 1 (
    echo ERROR: Alembic tidak terinstall!
    echo Jalankan setup.bat terlebih dahulu.
    pause
    exit /b 1
)

echo Menjalankan migrations...
python -m alembic upgrade head

if errorlevel 1 (
    echo.
    echo ERROR: Migration gagal!
    echo.
    echo Pastikan:
    echo 1. Database MySQL sudah berjalan
    echo 2. Database 'absenin' sudah dibuat
    echo 3. Konfigurasi di .env sudah benar
    echo.
    echo Lihat error message di atas untuk detail.
    pause
    exit /b 1
)

echo.
echo ========================================
echo Migrations berhasil!
echo ========================================
echo.
pause
