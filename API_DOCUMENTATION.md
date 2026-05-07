# 📚 API Documentation - AbsenIN (Role: Dosen)

## 🎯 Overview

API sederhana untuk sistem absensi dengan role **Dosen** yang memiliki akses penuh untuk mengelola:
- ✅ Mata Kuliah (CRUD)
- ✅ Mahasiswa (CRUD)
- ✅ Login & Authentication (JWT)

---

## 🔐 Authentication

### Login
```
POST /auth/login
```

**Request Body**:
```json
{
  "email": "dosen@absenin.local",
  "password": "dosen123"
}
```

**Response**:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "user": {
    "id": 1,
    "email": "dosen@absenin.local",
    "name": "Dosen"
  }
}
```

**Gunakan token di header**:
```
Authorization: Bearer <access_token>
```

---

## 📖 CRUD Mata Kuliah

### 1. Get All Mata Kuliah
```
GET /matakuliah
Authorization: Bearer <token>
```

**Query Parameters**:
- `skip` (optional): Offset untuk pagination (default: 0)
- `limit` (optional): Limit data (default: 100)

**Response**:
```json
[
  {
    "kode_mk": "KOM0001",
    "nama_mk": "Pemrograman Dasar",
    "sks": 3,
    "semester": 1
  },
  {
    "kode_mk": "KOM0002",
    "nama_mk": "Struktur Data",
    "sks": 3,
    "semester": 2
  }
]
```

---

### 2. Get Mata Kuliah by Kode
```
GET /matakuliah/{kode_mk}
Authorization: Bearer <token>
```

**Example**:
```
GET /matakuliah/KOM0001
```

**Response**:
```json
{
  "kode_mk": "KOM0001",
  "nama_mk": "Pemrograman Dasar",
  "sks": 3,
  "semester": 1
}
```

---

### 3. Create Mata Kuliah
```
POST /matakuliah
Authorization: Bearer <token>
Content-Type: application/json
```

**Request Body**:
```json
{
  "kode_mk": "KOM0009",
  "nama_mk": "Pemrograman Web",
  "sks": 3,
  "semester": 5
}
```

**Response** (201 Created):
```json
{
  "kode_mk": "KOM0009",
  "nama_mk": "Pemrograman Web",
  "sks": 3,
  "semester": 5
}
```

---

### 4. Update Mata Kuliah
```
PUT /matakuliah/{kode_mk}
Authorization: Bearer <token>
Content-Type: application/json
```

**Request Body** (semua field optional):
```json
{
  "nama_mk": "Pemrograman Web Lanjut",
  "sks": 4,
  "semester": 6
}
```

**Response**:
```json
{
  "kode_mk": "KOM0009",
  "nama_mk": "Pemrograman Web Lanjut",
  "sks": 4,
  "semester": 6
}
```

---

### 5. Delete Mata Kuliah
```
DELETE /matakuliah/{kode_mk}
Authorization: Bearer <token>
```

**Response**: 204 No Content

---

## 👨‍🎓 CRUD Mahasiswa

### 1. Get All Mahasiswa
```
GET /mahasiswa
Authorization: Bearer <token>
```

**Query Parameters**:
- `skip` (optional): Offset untuk pagination (default: 0)
- `limit` (optional): Limit data (default: 100)

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
  {
    "id_mahasiswa": 2,
    "nim": "J0403231019",
    "nama": "KEVIN FARHAN HERNANDEZ",
    "kelas": "B",
    "prodi": "TRPL"
  }
]
```

---

### 2. Get Mahasiswa by ID
```
GET /mahasiswa/{mahasiswa_id}
Authorization: Bearer <token>
```

**Example**:
```
GET /mahasiswa/1
```

**Response**:
```json
{
  "id_mahasiswa": 1,
  "nim": "J0403231006",
  "nama": "AZZAHRA NABILA CHAIRONA",
  "kelas": "A",
  "prodi": "TRPL"
}
```

---

### 3. Get Mahasiswa by NIM
```
GET /mahasiswa/nim/{nim}
Authorization: Bearer <token>
```

**Example**:
```
GET /mahasiswa/nim/J0403231006
```

**Response**:
```json
{
  "id_mahasiswa": 1,
  "nim": "J0403231006",
  "nama": "AZZAHRA NABILA CHAIRONA",
  "kelas": "A",
  "prodi": "TRPL"
}
```

---

### 4. Create Mahasiswa
```
POST /mahasiswa
Authorization: Bearer <token>
Content-Type: application/json
```

**Request Body**:
```json
{
  "nim": "J0403231999",
  "nama": "MAHASISWA BARU",
  "kelas": "A",
  "prodi": "TRPL"
}
```

**Response** (201 Created):
```json
{
  "id_mahasiswa": 17,
  "nim": "J0403231999",
  "nama": "MAHASISWA BARU",
  "kelas": "A",
  "prodi": "TRPL"
}
```

---

### 5. Update Mahasiswa
```
PUT /mahasiswa/{mahasiswa_id}
Authorization: Bearer <token>
Content-Type: application/json
```

**Request Body** (semua field optional):
```json
{
  "nama": "MAHASISWA BARU UPDATED",
  "kelas": "B",
  "prodi": "TRPL"
}
```

**Response**:
```json
{
  "id_mahasiswa": 17,
  "nim": "J0403231999",
  "nama": "MAHASISWA BARU UPDATED",
  "kelas": "B",
  "prodi": "TRPL"
}
```

---

### 6. Delete Mahasiswa
```
DELETE /mahasiswa/{mahasiswa_id}
Authorization: Bearer <token>
```

**Response**: 204 No Content

---

## 🧪 Testing dengan Postman

### Step 1: Login
1. **POST** `http://127.0.0.1:8000/auth/login`
2. Body:
   ```json
   {
     "email": "dosen@absenin.local",
     "password": "dosen123"
   }
   ```
3. Copy `access_token` dari response

### Step 2: Set Authorization
1. Tab "Authorization"
2. Type: "Bearer Token"
3. Token: Paste token dari login

### Step 3: Test CRUD

**Get All Mata Kuliah**:
- GET `http://127.0.0.1:8000/matakuliah`

**Create Mata Kuliah**:
- POST `http://127.0.0.1:8000/matakuliah`
- Body:
  ```json
  {
    "kode_mk": "KOM0009",
    "nama_mk": "Pemrograman Web",
    "sks": 3,
    "semester": 5
  }
  ```

**Get All Mahasiswa**:
- GET `http://127.0.0.1:8000/mahasiswa`

**Create Mahasiswa**:
- POST `http://127.0.0.1:8000/mahasiswa`
- Body:
  ```json
  {
    "nim": "J0403231999",
    "nama": "MAHASISWA BARU",
    "kelas": "A",
    "prodi": "TRPL"
  }
  ```

---

## 📊 Data yang Tersedia

### User (1):
- **Email**: dosen@absenin.local
- **Password**: dosen123
- **Role**: Dosen (Full Access)

### Mata Kuliah (8):
- KOM0001 - Pemrograman Dasar
- KOM0002 - Struktur Data
- KOM0003 - Algoritma dan Pemrograman
- KOM0004 - Basis Data
- KOM0005 - Sistem Operasi
- KOM0006 - Jaringan Komputer
- KOM0007 - Rekayasa Perangkat Lunak
- KOM0008 - Keamanan Siber

### Mahasiswa (16):
- J0403231006 - AZZAHRA NABILA CHAIRONA
- J0403231019 - KEVIN FARHAN HERNANDEZ
- J0403231031 - PUTI AISYAH LAILATULRAHMI
- J0403231035 - ARIO ELNINO
- Dan 12 lainnya...

---

## ❌ Error Responses

### 401 Unauthorized
```json
{
  "detail": "Token tidak valid atau sudah kadaluarsa"
}
```
**Solusi**: Login ulang untuk mendapatkan token baru

### 404 Not Found
```json
{
  "detail": "Mata kuliah tidak ditemukan"
}
```

### 400 Bad Request
```json
{
  "detail": "Kode mata kuliah sudah terdaftar"
}
```

---

## 🚀 Server Info

- **URL**: http://127.0.0.1:8000
- **API Docs**: http://127.0.0.1:8000/docs
- **Role**: Dosen (Full Access)
- **Database**: MySQL
- **Auth**: JWT Token

---

## 📝 Notes

- Semua endpoint (kecuali `/auth/login`) memerlukan JWT token
- Token expired setelah 30 menit (default)
- Dosen memiliki akses penuh untuk semua operasi CRUD
- NIM mahasiswa harus unique
- Kode mata kuliah harus unique

---

**Happy Coding!** 🚀
