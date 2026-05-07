@echo off
REM Script untuk menjalankan FastAPI server

REM Change to script directory
cd /d "%~dp0"

echo ========================================
echo Starting API-absenIN Server
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

echo Server akan berjalan di: http://localhost:8000
echo API Documentation: http://localhost:8000/docs
echo.
echo Tekan Ctrl+C untuk menghentikan server
echo.

python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
