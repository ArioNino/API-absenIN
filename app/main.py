from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import get_settings

# Import routers
from app.routes import auth, mahasiswa, matakuliah

settings = get_settings()

app = FastAPI(
    title=settings.APP_NAME,
    description="API untuk sistem absensi mahasiswa - Role: Dosen",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router)
app.include_router(mahasiswa.router)
app.include_router(matakuliah.router)

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
            "matakuliah": "/matakuliah"
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
