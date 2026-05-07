# 🔐 Quick Guide - JWT Token di Postman

## 🎯 2 Langkah Mudah

### 1️⃣ Login & Copy Token

**POST** `http://127.0.0.1:8000/auth/login`

Body:
```json
{
  "email": "dosen@absenin.local",
  "password": "dosen123"
}
```

Response:
```json
{
  "access_token": "eyJhbGci...",  ← COPY INI
  "token_type": "bearer"
}
```

---

### 2️⃣ Gunakan Token

**Di Postman**:
1. Tab **"Authorization"**
2. Type: **"Bearer Token"**
3. Token: **Paste token**
4. Send ✅

---

## 📋 Contoh Request

### Get Mahasiswa
```
GET http://127.0.0.1:8000/mahasiswa

Authorization Tab:
  Type: Bearer Token
  Token: eyJhbGci...
```

### Create Mata Kuliah
```
POST http://127.0.0.1:8000/matakuliah

Authorization Tab:
  Type: Bearer Token
  Token: eyJhbGci...

Body (JSON):
{
  "kode_mk": "KOM0009",
  "nama_mk": "Pemrograman Web",
  "sks": 3,
  "semester": 5
}
```

---

## ❌ Tanpa Token = Error 401

Request tanpa token akan gagal:
```json
{
  "detail": "Not authenticated"
}
```

---

## 🔄 Token Expired?

Token expired setelah 30 menit.

**Solusi**: Login ulang untuk dapat token baru.

---

## ✅ Endpoint yang Butuh Token

**Semua endpoint kecuali login**:
- ✅ GET /mahasiswa
- ✅ POST /mahasiswa
- ✅ PUT /mahasiswa/{id}
- ✅ DELETE /mahasiswa/{id}
- ✅ GET /matakuliah
- ✅ POST /matakuliah
- ✅ PUT /matakuliah/{kode}
- ✅ DELETE /matakuliah/{kode}

**Tidak butuh token**:
- ❌ POST /auth/login

---

**Lihat panduan lengkap**: `POSTMAN_TOKEN_GUIDE.md`

**Server**: http://127.0.0.1:8000  
**Docs**: http://127.0.0.1:8000/docs
