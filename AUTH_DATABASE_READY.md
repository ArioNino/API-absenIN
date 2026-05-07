# ✅ Setup Selesai - Auth dengan Database MySQL!

## 🎉 Yang Sudah Berhasil

1. ✅ **Email validator** terinstall
2. ✅ **Database MySQL** terhubung
3. ✅ **Migrations** berhasil dijalankan
4. ✅ **Seeders** berhasil mengisi data:
   - 2 Users (admin & dosen)
   - 1 Dosen
   - 8 Mata Kuliah
   - 6 Kelas
   - 16 Mahasiswa
5. ✅ **Server** berjalan dengan auth asli (JWT)

---

## 🔐 Test Login dengan Postman (Database Real)

### Endpoint
```
POST http://127.0.0.1:8000/auth/login
Content-Type: application/json
```

### Test Credentials (Dari Database)

#### Admin
```json
{
  "email": "admin@absenin.local",
  "password": "admin123"
}
```

#### Dosen
```json
{
  "email": "dosen@absenin.local",
  "password": "dosen123"
}
```

### Expected Response (JWT Token Real!)

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "user": {
    "id": 1,
    "email": "admin@absenin.local",
    "name": "Administrator"
  }
}
```

---

## 📝 Langkah Test di Postman

### 1. Login Request

**Method**: POST  
**URL**: `http://127.0.0.1:8000/auth/login`

**Headers**:
```
Content-Type: application/json
```

**Body** (raw JSON):
```json
{
  "email": "admin@absenin.local",
  "password": "admin123"
}
```

**Click**: Send

### 2. Response yang Didapat

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOjF9.xxx",
  "token_type": "bearer",
  "user": {
    "id": 1,
    "email": "admin@absenin.local",
    "name": "Administrator"
  }
}
```

### 3. Copy Token

Copy nilai `access_token` untuk digunakan di request berikutnya.

---

## 🔑 Perbedaan dengan Dummy Data

| Fitur | Dummy Data (Sebelum) | Database (Sekarang) |
|-------|---------------------|---------------------|
| **Token** | `dummy_token_1_...` | JWT Token Real |
| **Password** | Plain text | Bcrypt hashed |
| **Data** | In-memory | MySQL Database |
| **Persistent** | ❌ Hilang saat restart | ✅ Tersimpan |
| **Security** | ❌ Tidak aman | ✅ Aman |

---

## 🧪 Test Cases

### ✅ Login Berhasil

**Admin**:
```json
{
  "email": "admin@absenin.local",
  "password": "admin123"
}
```
Response: 200 OK + JWT Token

**Dosen**:
```json
{
  "email": "dosen@absenin.local",
  "password": "dosen123"
}
```
Response: 200 OK + JWT Token

### ❌ Login Gagal

**Email Salah**:
```json
{
  "email": "wrong@email.com",
  "password": "admin123"
}
```
Response: 401 Unauthorized
```json
{
  "detail": "Email tidak ditemukan"
}
```

**Password Salah**:
```json
{
  "email": "admin@absenin.local",
  "password": "wrongpassword"
}
```
Response: 401 Unauthorized
```json
{
  "detail": "Password salah"
}
```

---

## 🌐 Test di Browser (Swagger UI)

1. Buka: **http://127.0.0.1:8000/docs**
2. Scroll ke **POST /auth/login**
3. Click **"Try it out"**
4. Masukkan credentials
5. Click **"Execute"**
6. Lihat response dengan JWT token!

---

## 📊 Data yang Tersedia di Database

### Users (2)
- admin@absenin.local (Administrator)
- dosen@absenin.local (Dosen Test)

### Mahasiswa (16)
- AZZAHRA NABILA CHAIRONA (J0403231006)
- KEVIN FARHAN HERNANDEZ (J0403231019)
- PUTI AISYAH LAILATULRAHMI (J0403231031)
- ARIO ELNINO (J0403231035)
- Dan 12 lainnya...

### Mata Kuliah (8)
- Pemrograman Dasar
- Struktur Data
- Algoritma dan Pemrograman
- Basis Data
- Dan 4 lainnya...

### Kelas (6)
- Kelas A, B, C, D, E, F

---

## 🔧 Troubleshooting

### Error: "Email tidak ditemukan"
- Pastikan email benar: `admin@absenin.local` atau `dosen@absenin.local`
- Cek database: Data sudah di-seed

### Error: "Password salah"
- Password admin: `admin123`
- Password dosen: `dosen123`
- Password sudah di-hash dengan bcrypt

### Error: Connection refused
- Pastikan MySQL server berjalan
- Cek `.env` file untuk DATABASE_URL

---

## 🎯 Next Steps

Sekarang Anda bisa:
1. ✅ Login dengan JWT token real
2. ✅ Data tersimpan di MySQL
3. ✅ Password ter-hash dengan aman
4. ✅ Siap untuk development lanjutan

---

## 📚 File Penting

- **`app/main.py`** - Main app dengan auth router
- **`app/routes/auth.py`** - Login endpoint dengan JWT
- **`.env`** - Database configuration
- **`app/seed.py`** - Database seeder

---

**Server berjalan di**: http://127.0.0.1:8000  
**API Docs**: http://127.0.0.1:8000/docs

**Selamat! Auth dengan database MySQL sudah berjalan!** 🚀
