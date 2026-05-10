from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import get_settings

# Import routers
from app.routes import auth, mahasiswa, matakuliah, berita_acara, kehadiran, kelas

settings = get_settings()

app = FastAPI(
    title=settings.APP_NAME,
    description="API untuk sistem absensi mahasiswa - Role: Dosen",
    version="1.0.0"
)

# CORS middleware
# NOTE: browsers reject allow_origins=["*"] together with allow_credentials=True,
# so we disable credentials when the origin list is wildcard.
_cors_origins = settings.CORS_ORIGINS_LIST
_allow_credentials = _cors_origins != ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=_cors_origins,
    allow_credentials=_allow_credentials,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router)
app.include_router(mahasiswa.router)
app.include_router(matakuliah.router)
app.include_router(kelas.router)
app.include_router(berita_acara.router)
app.include_router(kehadiran.router)

@app.get("/")
def read_root():
    """Root endpoint - Hello World"""
    return {
        "message": "Hello World from AbsenIN API!",
        "status": "running",
        "version": "1.0.0",
        "role": "Dosen (Full Access)",
        "database": "MySQL",
        "endpoints": {
            "docs": "/docs",
            "login": "/auth/login",
            "mahasiswa": "/mahasiswa",
            "matakuliah": "/matakuliah",
            "kelas": "/kelas",
            "berita_acara": "/berita-acara",
            "kehadiran": "/kehadiran"
        }
    }

@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "AbsenIN API",
        "database": "MySQL",
        "role": "Dosen"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
