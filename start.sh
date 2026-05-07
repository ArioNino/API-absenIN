#!/bin/bash
# Start script untuk Linux/Mac

echo "========================================="
echo "Starting AbsenIN API Server"
echo "========================================="
echo ""
echo "Server: http://0.0.0.0:8000"
echo "API Docs: http://0.0.0.0:8000/docs"
echo ""
echo "Login Credentials:"
echo "- Email: dosen@absenin.local"
echo "- Password: dosen123"
echo ""
echo "Press Ctrl+C to stop server"
echo ""

# Activate virtual environment
source .venv/bin/activate

# Start server
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
