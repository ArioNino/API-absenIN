@echo off
REM Script untuk menghapus virtual environment secara paksa

REM Change to script directory
cd /d "%~dp0"

echo ========================================
echo Force Delete Virtual Environment
echo ========================================
echo.
echo Working directory: %CD%
echo.

if not exist venv (
    echo Folder venv tidak ditemukan.
    echo Tidak ada yang perlu dihapus.
    pause
    exit /b 0
)

echo WARNING: Script ini akan menghapus folder venv secara paksa!
echo.
set /p confirm="Lanjutkan? (Y/N): "
if /i not "%confirm%"=="Y" (
    echo Dibatalkan.
    pause
    exit /b 0
)

echo.
echo [1/4] Menonaktifkan virtual environment...
call venv\Scripts\deactivate.bat 2>nul
echo.

echo [2/4] Menunggu proses selesai...
timeout /t 3 /nobreak >nul
echo.

echo [3/4] Menghapus folder venv...
rmdir /s /q venv 2>nul

if exist venv (
    echo Mencoba dengan metode alternatif...
    rd /s /q venv 2>nul
    timeout /t 2 /nobreak >nul
)

echo.
echo [4/4] Verifikasi...
if exist venv (
    echo.
    echo ========================================
    echo GAGAL: Folder venv masih ada!
    echo ========================================
    echo.
    echo Folder venv tidak bisa dihapus karena:
    echo - Ada proses yang masih menggunakan file di dalamnya
    echo - File sedang dibuka oleh program lain
    echo.
    echo SOLUSI MANUAL:
    echo.
    echo 1. Tutup SEMUA aplikasi berikut:
    echo    - Command Prompt / PowerShell
    echo    - VS Code / PyCharm / IDE lainnya
    echo    - Python processes (cek Task Manager)
    echo.
    echo 2. Restart komputer (jika perlu)
    echo.
    echo 3. Hapus folder venv secara manual:
    echo    - Buka File Explorer
    echo    - Navigasi ke: %CD%
    echo    - Klik kanan folder "venv"
    echo    - Pilih "Delete"
    echo.
    echo 4. Jalankan setup.bat
    echo.
    pause
    exit /b 1
) else (
    echo.
    echo ========================================
    echo BERHASIL: Folder venv telah dihapus!
    echo ========================================
    echo.
    echo Sekarang Anda bisa menjalankan:
    echo   setup.bat
    echo.
    pause
    exit /b 0
)
