# 🚀 Quick Reference - Test Login dengan Postman

## 📍 Endpoint Login

```
POST http://127.0.0.1:8000/auth/login
Content-Type: application/json
```

## 🔑 Test Credentials

### Admin
```json
{
  "email": "admin@absenin.local",
  "password": "admin123"
}
```

### Dosen
```json
{
  "email": "dosen@absenin.local",
  "password": "dosen123"
}
```

### Mahasiswa
```json
{
  "email": "mahasiswa@absenin.local",
  "password": "mahasiswa123"
}
```

## ✅ Expected Response (Success)

```json
{
  "status": "success",
  "message": "Login berhasil",
  "token": "dummy_token_1_admin@absenin.local",
  "user": {
    "id": 1,
    "email": "admin@absenin.local",
    "name": "Administrator",
    "role": "admin"
  }
}
```

## ❌ Error Responses

### Email Salah (401)
```json
{
  "detail": "Email tidak ditemukan"
}
```

### Password Salah (401)
```json
{
  "detail": "Password salah"
}
```

## 📝 Langkah di Postman

1. **Method**: POST
2. **URL**: `http://127.0.0.1:8000/auth/login`
3. **Headers**: 
   - Content-Type: application/json
4. **Body**: 
   - Pilih "raw" dan "JSON"
   - Copy salah satu credential di atas
5. **Send**: Klik tombol Send
6. **Result**: Lihat response di bawah

## 🌐 Test di Browser

Buka: http://127.0.0.1:8000/docs

1. Cari endpoint `/auth/login`
2. Klik "Try it out"
3. Masukkan email dan password
4. Klik "Execute"
5. Lihat response

---

**Lihat panduan lengkap di**: `POSTMAN_TESTING.md`
