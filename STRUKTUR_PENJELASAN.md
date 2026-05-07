# 📁 Struktur Project - Penjelasan

## ✅ Sekarang Sudah Terhubung!

Login endpoint sekarang menggunakan **Router** yang proper:

```
app/main.py
    ↓ (include_router)
app/routes/auth_simple.py
    ↓ (router.post)
@router.post("/auth/login")
```

## 📂 Struktur File

```
API-absenIN/
├── app/
│   ├── main.py                    # ✅ Main app (include routers)
│   ├── routes/
│   │   ├── auth_simple.py         # ✅ Login endpoint (AKTIF - dummy data)
│   │   ├── auth.py                # ❌ Login dengan JWT (butuh database)
│   │   ├── mahasiswa.py           # ❌ CRUD mahasiswa (butuh database)
│   │   ├── kehadiran.py           # ❌ CRUD kehadiran (butuh database)
│   │   └── berita_acara.py        # ❌ CRUD BAP (butuh database)
│   ├── models/                    # Database models (tidak dipakai sekarang)
│   ├── schemas/                   # Pydantic schemas (tidak dipakai sekarang)
│   └── utils/                     # Utilities (tidak dipakai sekarang)
└── .venv/                         # Virtual environment
```

## 🔄 Alur Request

### Login Request Flow:

```
1. Client (Postman/Browser)
   ↓
   POST http://127.0.0.1:8000/auth/login
   Body: {"email": "admin@absenin.local", "password": "admin123"}
   ↓
2. FastAPI (app/main.py)
   ↓
   app.include_router(auth_simple.router)
   ↓
3. Router (app/routes/auth_simple.py)
   ↓
   @router.post("/login")
   def login(request: LoginRequest):
   ↓
4. Logic:
   - Cari user di users_data (dummy)
   - Validasi password
   - Generate token
   ↓
5. Response
   {
     "status": "success",
     "token": "dummy_token_...",
     "user": {...}
   }
```

## 📝 Perbedaan 2 Versi Auth

### 1. auth_simple.py (✅ AKTIF SEKARANG)
```python
# File: app/routes/auth_simple.py
router = APIRouter(prefix="/auth", tags=["Authentication"])

# Data dummy di file
users_data = [...]

@router.post("/login")
def login(request: LoginRequest):
    # Cari di dummy data
    user = next((u for u in users_data if u["email"] == request.email), None)
    # Return dummy token
    return {"token": "dummy_token_..."}
```

**Keuntungan**:
- ✅ Tidak butuh database
- ✅ Langsung jalan
- ✅ Mudah testing

**Kekurangan**:
- ❌ Data hilang saat restart
- ❌ Tidak ada JWT real
- ❌ Password tidak di-hash

---

### 2. auth.py (❌ TIDAK AKTIF - Butuh Database)
```python
# File: app/routes/auth.py
router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/login", response_model=TokenResponse)
def login(data: LoginSchema, db: Session = Depends(get_db)):
    # Query dari database
    user = db.query(User).filter(User.email == data.email).first()
    # Verify password hash
    verify_password(data.password, user.password)
    # Generate JWT token
    access_token = create_access_token(data={"sub": user.id})
    return TokenResponse(access_token=access_token, ...)
```

**Keuntungan**:
- ✅ Data persistent di database
- ✅ JWT token real
- ✅ Password di-hash dengan bcrypt
- ✅ Lebih secure

**Kekurangan**:
- ❌ Butuh MySQL running
- ❌ Butuh migration
- ❌ Lebih kompleks

---

## 🎯 Endpoint Mapping

| URL | File | Status |
|-----|------|--------|
| `POST /auth/login` | `routes/auth_simple.py` | ✅ Aktif |
| `GET /` | `main.py` | ✅ Aktif |
| `GET /mahasiswa` | `main.py` | ✅ Aktif |
| `GET /kehadiran` | `main.py` | ✅ Aktif |
| `GET /stats` | `main.py` | ✅ Aktif |

## 🔄 Cara Upgrade ke Database (Nanti)

Ketika MySQL sudah ready:

1. **Ganti import di main.py**:
```python
# Dari:
from app.routes import auth_simple

# Ke:
from app.routes import auth, mahasiswa, kehadiran
```

2. **Ganti router**:
```python
# Dari:
app.include_router(auth_simple.router)

# Ke:
app.include_router(auth.router)
app.include_router(mahasiswa.router)
app.include_router(kehadiran.router)
```

3. **Hapus endpoint dummy di main.py**

4. **Jalankan migration**:
```bash
.venv\Scripts\python.exe -m alembic upgrade head
```

5. **Jalankan seeder**:
```bash
.venv\Scripts\python.exe -m app.seed
```

## 📊 Perbandingan

| Fitur | Sekarang (Dummy) | Nanti (Database) |
|-------|------------------|------------------|
| Login | ✅ Dummy token | ✅ JWT token |
| Data | ✅ In-memory | ✅ MySQL |
| Password | ❌ Plain text | ✅ Bcrypt hash |
| Persistent | ❌ Hilang saat restart | ✅ Tersimpan |
| Setup | ✅ Mudah | ⚠️ Butuh MySQL |

## 💡 Kesimpulan

**Sekarang**: Login endpoint sudah **terhubung dengan router** (`auth_simple.py`) dan menggunakan struktur yang lebih rapi!

**Struktur**:
```
main.py → include_router → auth_simple.py → @router.post("/login")
```

**Test di Postman**:
```
POST http://127.0.0.1:8000/auth/login
Body: {"email": "admin@absenin.local", "password": "admin123"}
```

✅ **Sudah proper dan terstruktur dengan baik!**
