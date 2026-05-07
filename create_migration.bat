@echo off
REM Script untuk membuat migration baru

REM Change to script directory
cd /d "%~dp0"

echo ========================================
echo Create New Alembic Migration
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

if "%~1"=="" (
    echo ERROR: Nama migration tidak diberikan!
    echo.
    echo Cara penggunaan:
    echo   create_migration.bat "nama_migration"
    echo.
    echo Contoh:
    echo   create_migration.bat "add_timestamps_to_models"
    echo.
    pause
    exit /b 1
)

echo Membuat migration: %~1
python -m alembic revision --autogenerate -m "%~1"

if errorlevel 1 (
    echo.
    echo ERROR: Gagal membuat migration!
    echo.
    echo Pastikan:
    echo 1. Database connection di .env sudah benar
    echo 2. Models sudah diimport dengan benar
    echo.
    echo Lihat error message di atas untuk detail.
    pause
    exit /b 1
)

echo.
echo ========================================
echo Migration berhasil dibuat!
echo ========================================
echo.
echo File migration baru ada di folder: alembic\versions\
echo.
echo Langkah selanjutnya:
echo 1. Review file migration yang dibuat
echo 2. Jalankan: run_migration.bat
echo.
pause
