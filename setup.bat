@echo off
REM Setup script untuk API-absenIN
REM Script ini akan membuat virtual environment baru dan install dependencies

REM Change to script directory
cd /d "%~dp0"

echo ========================================
echo API-absenIN Setup Script
echo ========================================
echo.
echo Working directory: %CD%
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python tidak ditemukan!
    echo Silakan install Python terlebih dahulu dari https://www.python.org/
    pause
    exit /b 1
)

REM Check if requirements.txt exists
if not exist requirements.txt (
    echo ERROR: File requirements.txt tidak ditemukan!
    echo Pastikan Anda menjalankan script ini dari folder project.
    pause
    exit /b 1
)

echo [1/5] Menghapus virtual environment lama (jika ada)...
if exist venv (
    echo Menonaktifkan virtual environment yang aktif...
    call venv\Scripts\deactivate.bat 2>nul
    
    echo Menunggu 2 detik...
    timeout /t 2 /nobreak >nul
    
    echo Menghapus folder venv...
    rmdir /s /q venv 2>nul
    
    REM Jika masih gagal, coba dengan rd
    if exist venv (
        echo Mencoba menghapus dengan metode alternatif...
        rd /s /q venv 2>nul
        timeout /t 1 /nobreak >nul
    )
    
    REM Cek apakah berhasil dihapus
    if exist venv (
        echo.
        echo ========================================
        echo WARNING: Tidak bisa menghapus folder venv!
        echo ========================================
        echo.
        echo Kemungkinan ada proses yang masih menggunakan file di dalamnya.
        echo.
        echo SOLUSI:
        echo 1. Tutup SEMUA terminal/command prompt yang terbuka
        echo 2. Tutup VS Code atau IDE lainnya yang membuka project ini
        echo 3. Tutup Python processes yang berjalan (cek Task Manager)
        echo 4. Jalankan setup.bat lagi
        echo.
        echo ATAU hapus folder venv secara manual:
        echo 1. Tutup window ini
        echo 2. Buka File Explorer
        echo 3. Hapus folder "venv" (klik kanan - Delete)
        echo 4. Jalankan setup.bat lagi
        echo.
        pause
        exit /b 1
    )
    
    echo Virtual environment lama berhasil dihapus.
) else (
    echo Tidak ada virtual environment lama.
)
echo.

echo [2/5] Membuat virtual environment baru...
python -m venv venv
if errorlevel 1 (
    echo ERROR: Gagal membuat virtual environment!
    echo.
    echo Kemungkinan penyebab:
    echo 1. Python tidak terinstall dengan benar
    echo 2. Tidak ada permission untuk membuat folder
    echo 3. Disk space tidak cukup
    echo.
    pause
    exit /b 1
)
echo Virtual environment berhasil dibuat.
echo.

echo [3/5] Mengaktifkan virtual environment...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo ERROR: Gagal mengaktifkan virtual environment!
    pause
    exit /b 1
)
echo Virtual environment aktif.
echo.

echo [4/5] Menginstall dependencies...
echo Upgrading pip...
python -m pip install --upgrade pip --quiet
echo.
echo Installing packages from requirements.txt...
echo (Ini mungkin memakan waktu beberapa menit...)
echo.
pip install -r requirements.txt
if errorlevel 1 (
    echo.
    echo ERROR: Gagal menginstall dependencies!
    echo.
    echo Troubleshooting:
    echo 1. Pastikan koneksi internet aktif
    echo 2. Coba jalankan manual: pip install -r requirements.txt
    echo 3. Lihat error message di atas untuk detail
    pause
    exit /b 1
)
echo.
echo Dependencies berhasil diinstall.
echo.

echo [5/5] Memeriksa file .env...
if not exist .env (
    echo WARNING: File .env tidak ditemukan!
    if exist .env.example (
        echo Membuat .env dari .env.example...
        copy .env.example .env >nul
        echo File .env berhasil dibuat.
    ) else (
        echo ERROR: File .env.example tidak ditemukan!
        echo Silakan buat file .env secara manual.
    )
    echo.
    echo PENTING: Edit file .env dan sesuaikan konfigurasi database Anda!
    echo.
) else (
    echo File .env sudah ada.
)
echo.

echo ========================================
echo Setup selesai!
echo ========================================
echo.
echo Langkah selanjutnya:
echo 1. Edit file .env dan sesuaikan konfigurasi database
echo    (Buka dengan: notepad .env)
echo.
echo 2. Buat database MySQL:
echo    mysql -u root -p
echo    CREATE DATABASE absenin;
echo.
echo 3. Jalankan migrations:
echo    run_migration.bat
echo.
echo 4. (Opsional) Seed data contoh:
echo    run_seed.bat
echo.
echo 5. Jalankan server:
echo    run_server.bat
echo.
pause
