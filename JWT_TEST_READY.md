# ✅ JWT Token Sudah Diperbaiki!

## 🔧 Masalah yang Diperbaiki

**Error**: `Subject must be a string`

**Penyebab**: JWT library mengharapkan 'sub' (subject) sebagai string, tapi kita passing integer.

**Solusi**:
1. ✅ Convert `user.id` ke `str(user.id)` saat create token
2. ✅ Convert `sub` dari string ke int saat decode token

---

## 🧪 Test JWT Sekarang

### Step 1: Login untuk Dapat Token Baru

**POST** `http://127.0.0.1:8000/auth/login`

**Body**:
```json
{
  "email": "dosen@absenin.local",
  "password": "dosen123"
}
```

**Response** (Token Baru - Fixed!):
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZXhwIjoxNzc4MTY4ODM2fQ...",
  "token_type": "bearer",
  "user": {
    "email": "dosen@absenin.local",
    "name": "Dosen",
    "id": 1
  }
}
```

**Perhatikan**: `"sub":"1"` (string) bukan `"sub":1` (integer)

---

### Step 2: Test Token di Postman

**1. Copy Token**
Copy `access_token` dari response login

**2. Test Endpoint Protected**
```
GET http://127.0.0.1:8000/mahasiswa

Authorization Tab:
  Type: Bearer Token
  Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Expected Response** (200 OK):
```json
[
  {
    "id_mahasiswa": 1,
    "nim": "J0403231006",
    "nama": "AZZAHRA NABILA CHAIRONA",
    "kelas": "A",
    "prodi": "TRPL"
  },
  ...
]
```

---

### Step 3: Test CRUD Operations

#### Create Mata Kuliah
```
POST http://127.0.0.1:8000/matakuliah
Authorization: Bearer <token>
Body:
{
  "kode_mk": "KOM0009",
  "nama_mk": "Pemrograman Web",
  "sks": 3,
  "semester": 5
}
```

#### Create Mahasiswa
```
POST http://127.0.0.1:8000/mahasiswa
Authorization: Bearer <token>
Body:
{
  "nim": "J0403231999",
  "nama": "MAHASISWA BARU",
  "kelas": "A",
  "prodi": "TRPL"
}
```

#### Update Mahasiswa
```
PUT http://127.0.0.1:8000/mahasiswa/17
Authorization: Bearer <token>
Body:
{
  "nama": "MAHASISWA UPDATED"
}
```

#### Delete Mahasiswa
```
DELETE http://127.0.0.1:8000/mahasiswa/17
Authorization: Bearer <token>
```

---

## ❌ Test Error Cases

### Tanpa Token (401)
```
GET http://127.0.0.1:8000/mahasiswa
(tanpa Authorization header)

Response: 401 Unauthorized
{
  "detail": "Not authenticated"
}
```

### Token Invalid (401)
```
GET http://127.0.0.1:8000/mahasiswa
Authorization: Bearer invalid_token_here

Response: 401 Unauthorized
{
  "detail": "Token tidak valid atau sudah kadaluarsa"
}
```

---

## 📊 Data yang Tersedia

### Mata Kuliah (8)
- KOM0001 - Pemrograman Dasar
- KOM0002 - Struktur Data
- KOM0003 - Algoritma dan Pemrograman
- KOM0004 - Basis Data
- KOM0005 - Sistem Operasi
- KOM0006 - Jaringan Komputer
- KOM0007 - Rekayasa Perangkat Lunak
- KOM0008 - Keamanan Siber

### Mahasiswa (16)
- J0403231006 - AZZAHRA NABILA CHAIRONA
- J0403231019 - KEVIN FARHAN HERNANDEZ
- J0403231031 - PUTI AISYAH LAILATULRAHMI
- J0403231035 - ARIO ELNINO
- Dan 12 lainnya...

---

## 🔒 Security Status

✅ **All endpoints protected** dengan JWT
✅ **Password hashed** dengan bcrypt
✅ **Token validation** working
✅ **Role-based access** (Dosen)

---

## 🎯 Quick Test Checklist

- [ ] Login berhasil → dapat JWT token
- [ ] GET /mahasiswa dengan token → 200 OK
- [ ] GET /matakuliah dengan token → 200 OK
- [ ] POST /mahasiswa dengan token → 201 Created
- [ ] POST /matakuliah dengan token → 201 Created
- [ ] PUT /mahasiswa/{id} dengan token → 200 OK
- [ ] DELETE /mahasiswa/{id} dengan token → 204 No Content
- [ ] Request tanpa token → 401 Unauthorized

---

## 🌐 Server Info

- **URL**: http://127.0.0.1:8000
- **Docs**: http://127.0.0.1:8000/docs (Interactive API)
- **Status**: ✅ Running dengan JWT fix
- **Auth**: ✅ JWT token working

---

**JWT token sudah diperbaiki dan siap digunakan!** 🚀

Gunakan token baru dari login untuk test semua endpoint protected.
