# 🔐 Panduan Menggunakan JWT Token di Postman

## 📋 Overview

Semua endpoint API (kecuali `/auth/login`) memerlukan JWT token untuk akses. Panduan ini menjelaskan cara menggunakan token di Postman.

---

## 🎯 Step-by-Step Guide

### Step 1: Login untuk Mendapatkan Token

**1. Buat Request Baru di Postman**
- Klik "New" → "HTTP Request"

**2. Set Request Details**
- **Method**: `POST`
- **URL**: `http://127.0.0.1:8000/auth/login`

**3. Set Headers**
- Tab "Headers"
- Add:
  - Key: `Content-Type`
  - Value: `application/json`

**4. Set Body**
- Tab "Body"
- Pilih "raw"
- Pilih "JSON" dari dropdown
- Masukkan:
```json
{
  "email": "dosen@absenin.local",
  "password": "dosen123"
}
```

**5. Send Request**
- Klik tombol "Send"

**6. Copy Token dari Response**
Response akan seperti ini:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOjEsImV4cCI6MTcxNTEwMjQwMH0.xxx",
  "token_type": "bearer",
  "user": {
    "id": 1,
    "email": "dosen@absenin.local",
    "name": "Dosen"
  }
}
```

**Copy nilai `access_token`** (tanpa tanda kutip)

---

### Step 2: Menggunakan Token di Request Lain

Ada **2 cara** menggunakan token di Postman:

---

## 🔑 Cara 1: Authorization Tab (RECOMMENDED)

**1. Buat Request Baru** (misal: GET Mahasiswa)
- Method: `GET`
- URL: `http://127.0.0.1:8000/mahasiswa`

**2. Tab "Authorization"**
- Klik tab "Authorization"
- Type: Pilih **"Bearer Token"** dari dropdown
- Token: **Paste token** yang sudah di-copy

**3. Send**
- Klik "Send"
- ✅ Request berhasil!

### Screenshot:
```
┌─────────────────────────────────────────┐
│ Authorization                           │
├─────────────────────────────────────────┤
│ Type: Bearer Token          [▼]         │
│                                         │
│ Token: eyJhbGciOiJIUzI1NiIsInR5cCI6... │
│                                         │
└─────────────────────────────────────────┘
```

---

## 🔑 Cara 2: Manual Header

**1. Buat Request Baru**
- Method: `GET`
- URL: `http://127.0.0.1:8000/mahasiswa`

**2. Tab "Headers"**
- Add header:
  - Key: `Authorization`
  - Value: `Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6...` (dengan prefix "Bearer ")

**⚠️ PENTING**: Harus ada spasi setelah "Bearer"!

**3. Send**
- Klik "Send"
- ✅ Request berhasil!

---

## 📝 Contoh Request dengan Token

### Get All Mahasiswa

**Request**:
```
GET http://127.0.0.1:8000/mahasiswa
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6...
```

**Response**:
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

### Create Mata Kuliah

**Request**:
```
POST http://127.0.0.1:8000/matakuliah
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6...
Content-Type: application/json

Body:
{
  "kode_mk": "KOM0009",
  "nama_mk": "Pemrograman Web",
  "sks": 3,
  "semester": 5
}
```

**Response**:
```json
{
  "kode_mk": "KOM0009",
  "nama_mk": "Pemrograman Web",
  "sks": 3,
  "semester": 5
}
```

---

## 🔄 Menggunakan Environment Variables (Advanced)

Untuk memudahkan, simpan token di environment variable:

### 1. Buat Environment
- Klik icon "⚙️" (Settings) di kanan atas
- Pilih "Environments"
- Klik "Add"
- Nama: "AbsenIN Local"

### 2. Tambah Variable
- Variable: `token`
- Initial Value: (kosongkan)
- Current Value: (kosongkan)

### 3. Auto-Save Token Setelah Login

Di request login, tab "Tests", tambahkan script:
```javascript
// Parse response
var jsonData = pm.response.json();

// Save token to environment
if (jsonData.access_token) {
    pm.environment.set("token", jsonData.access_token);
    console.log("Token saved!");
}
```

### 4. Gunakan Variable di Request Lain

Di tab "Authorization":
- Type: Bearer Token
- Token: `{{token}}`

Atau di Headers:
- Key: `Authorization`
- Value: `Bearer {{token}}`

---

## ❌ Error Responses

### 401 Unauthorized - Token Tidak Ada
```json
{
  "detail": "Not authenticated"
}
```
**Solusi**: Tambahkan token di Authorization header

### 401 Unauthorized - Token Invalid
```json
{
  "detail": "Token tidak valid atau sudah kadaluarsa"
}
```
**Solusi**: Login ulang untuk mendapatkan token baru

### 401 Unauthorized - Token Expired
```json
{
  "detail": "Token tidak valid atau sudah kadaluarsa"
}
```
**Solusi**: Login ulang (token expired setelah 30 menit)

---

## 🧪 Testing Checklist

### ✅ Test 1: Login
- [ ] POST `/auth/login` berhasil
- [ ] Dapat `access_token`
- [ ] Token di-copy

### ✅ Test 2: Get dengan Token
- [ ] GET `/mahasiswa` dengan token berhasil
- [ ] GET `/matakuliah` dengan token berhasil

### ✅ Test 3: Create dengan Token
- [ ] POST `/mahasiswa` dengan token berhasil
- [ ] POST `/matakuliah` dengan token berhasil

### ✅ Test 4: Update dengan Token
- [ ] PUT `/mahasiswa/{id}` dengan token berhasil
- [ ] PUT `/matakuliah/{kode}` dengan token berhasil

### ✅ Test 5: Delete dengan Token
- [ ] DELETE `/mahasiswa/{id}` dengan token berhasil
- [ ] DELETE `/matakuliah/{kode}` dengan token berhasil

### ❌ Test 6: Tanpa Token (Harus Gagal)
- [ ] GET `/mahasiswa` tanpa token → 401
- [ ] POST `/matakuliah` tanpa token → 401

---

## 💡 Tips & Tricks

### 1. Save Request ke Collection
Simpan semua request ke collection untuk reuse:
- Klik "Save" setelah membuat request
- Buat collection: "AbsenIN API"
- Organize by folder: Auth, Mahasiswa, Mata Kuliah

### 2. Duplicate Request
Untuk membuat request serupa:
- Klik "..." di request
- Pilih "Duplicate"
- Edit URL dan body

### 3. Token Expired?
Token expired setelah 30 menit. Jika dapat error 401:
1. Login ulang
2. Copy token baru
3. Update di Authorization tab

### 4. Test Multiple Scenarios
Buat request untuk:
- ✅ Success case (dengan token valid)
- ❌ Error case (tanpa token)
- ❌ Error case (token invalid)

---

## 📸 Visual Guide

### Login Request
```
POST http://127.0.0.1:8000/auth/login

Headers:
  Content-Type: application/json

Body (raw JSON):
{
  "email": "dosen@absenin.local",
  "password": "dosen123"
}

Response:
{
  "access_token": "eyJhbGci...",  ← COPY INI
  "token_type": "bearer",
  "user": {...}
}
```

### Protected Request
```
GET http://127.0.0.1:8000/mahasiswa

Authorization:
  Type: Bearer Token
  Token: eyJhbGci...  ← PASTE DI SINI

Response:
[
  {
    "id_mahasiswa": 1,
    "nim": "J0403231006",
    ...
  }
]
```

---

## 🎯 Quick Reference

| Endpoint | Method | Auth Required | Description |
|----------|--------|---------------|-------------|
| `/auth/login` | POST | ❌ No | Login untuk dapat token |
| `/mahasiswa` | GET | ✅ Yes | List mahasiswa |
| `/mahasiswa/{id}` | GET | ✅ Yes | Get mahasiswa by ID |
| `/mahasiswa` | POST | ✅ Yes | Create mahasiswa |
| `/mahasiswa/{id}` | PUT | ✅ Yes | Update mahasiswa |
| `/mahasiswa/{id}` | DELETE | ✅ Yes | Delete mahasiswa |
| `/matakuliah` | GET | ✅ Yes | List mata kuliah |
| `/matakuliah/{kode}` | GET | ✅ Yes | Get mata kuliah |
| `/matakuliah` | POST | ✅ Yes | Create mata kuliah |
| `/matakuliah/{kode}` | PUT | ✅ Yes | Update mata kuliah |
| `/matakuliah/{kode}` | DELETE | ✅ Yes | Delete mata kuliah |

---

## 🔒 Security Notes

- ✅ Token disimpan di memory Postman (aman untuk development)
- ✅ Token expired setelah 30 menit
- ✅ Harus login ulang setelah token expired
- ⚠️ Jangan share token ke orang lain
- ⚠️ Jangan commit token ke git

---

**Sekarang Anda siap menggunakan API dengan JWT token di Postman!** 🚀

**Server**: http://127.0.0.1:8000  
**Docs**: http://127.0.0.1:8000/docs
