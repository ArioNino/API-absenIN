@echo off
echo ========================================
echo AbsenIN API Server
echo ========================================
echo.
echo Server: http://127.0.0.1:8000
echo API Docs: http://127.0.0.1:8000/docs
echo.
echo Login Credentials:
echo - Email: dosen@absenin.local
echo - Password: dosen123
echo.
echo Dokumentasi:
echo - API_REQUEST_GUIDE.md (Request body lengkap)
echo - REQUEST_QUICK_GUIDE.md (Quick reference)
echo - CRUD_RESPONSES.md (Response format)
echo.
echo Tekan Ctrl+C untuk stop server
echo.

.venv\Scripts\python.exe -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
