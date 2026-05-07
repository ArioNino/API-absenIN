# 📝 Panduan Lengkap Request API - AbsenIN

## 🔐 Authentication

Semua endpoint (kecuali login) memerlukan JWT token di header:
```
Authorization: Bearer <your_jwt_token>
```

---

## 👨‍🎓 MAHASISWA CRUD

### 1. CREATE Mahasiswa (POST)

**Endpoint**: `POST http://127.0.0.1:8000/mahasiswa`

**Headers**:
```
Authorization: Bearer <token>
Content-Type: application/json
```

**Request Body** (Semua field WAJIB):
```json
{
  "nim": "J0403231999",
  "nama": "NAMA LENGKAP MAHASISWA",
  "kelas": "A",
  "prodi": "TRPL"
}
```

**Field Requirements**:
- `nim` (string, required) - NIM mahasiswa, harus unique
- `nama` (string, required) - Nama lengkap mahasiswa
- `kelas` (string, required) - Kelas mahasiswa (contoh: A, B, C)
- `prodi` (string, required) - Program studi (contoh: TRPL, JMP)

**Response Success (201 Created)**:
```json
{
  "message": "Mahasiswa berhasil ditambahkan",
  "data": {
    "id_mahasiswa": 18,
    "nim": "J0403231999",
    "nama": "NAMA LENGKAP MAHASISWA",
    "kelas": "A",
    "prodi": "TRPL"
  }
}
```

**Response Error (400 Bad Request)** - NIM sudah ada:
```json
{
  "detail": "NIM sudah terdaftar"
}
```

**Response Error (401 Unauthorized)** - Token tidak valid:
```json
{
  "detail": "Token tidak valid atau sudah kadaluarsa"
}
```

---

### 2. GET All Mahasiswa

**Endpoint**: `GET http://127.0.0.1:8000/mahasiswa`

**Headers**:
```
Authorization: Bearer <token>
```

**Query Parameters** (Optional):
- `skip` (integer, default: 0) - Untuk pagination
- `limit` (integer, default: 100) - Jumlah data per page

**Example**:
```
GET http://127.0.0.1:8000/mahasiswa?skip=0&limit=10
```

**Response Success (200 OK)**:
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

### 3. GET Mahasiswa by ID

**Endpoint**: `GET http://127.0.0.1:8000/mahasiswa/{id}`

**Headers**:
```
Authorization: Bearer <token>
```

**Example**:
```
GET http://127.0.0.1:8000/mahasiswa/1
```

**Response Success (200 OK)**:
```json
{
  "id_mahasiswa": 1,
  "nim": "J0403231006",
  "nama": "AZZAHRA NABILA CHAIRONA",
  "kelas": "A",
  "prodi": "TRPL"
}
```

**Response Error (404 Not Found)**:
```json
{
  "detail": "Mahasiswa tidak ditemukan"
}
```

---

### 4. GET Mahasiswa by NIM

**Endpoint**: `GET http://127.0.0.1:8000/mahasiswa/nim/{nim}`

**Headers**:
```
Authorization: Bearer <token>
```

**Example**:
```
GET http://127.0.0.1:8000/mahasiswa/nim/J0403231006
```

**Response**: Sama seperti GET by ID

---

### 5. UPDATE Mahasiswa (PUT)

**Endpoint**: `PUT http://127.0.0.1:8000/mahasiswa/{id}`

**Headers**:
```
Authorization: Bearer <token>
Content-Type: application/json
```

**Request Body** (Semua field OPTIONAL - kirim hanya yang ingin diupdate):
```json
{
  "nim": "J0403231999",
  "nama": "NAMA BARU",
  "kelas": "B",
  "prodi": "JMP"
}
```

**Example - Update hanya nama**:
```json
{
  "nama": "AZZAHRA NABILA (UPDATED)"
}
```

**Example - Update nama dan kelas**:
```json
{
  "nama": "AZZAHRA NABILA",
  "kelas": "B"
}
```

**Response Success (200 OK)**:
```json
{
  "message": "Mahasiswa berhasil diupdate",
  "data": {
    "id_mahasiswa": 1,
    "nim": "J0403231006",
    "nama": "AZZAHRA NABILA (UPDATED)",
    "kelas": "B",
    "prodi": "TRPL"
  }
}
```

**Response Error (404 Not Found)**:
```json
{
  "detail": "Mahasiswa tidak ditemukan"
}
```

**Response Error (400 Bad Request)** - NIM baru sudah dipakai:
```json
{
  "detail": "NIM sudah terdaftar"
}
```

---

### 6. DELETE Mahasiswa

**Endpoint**: `DELETE http://127.0.0.1:8000/mahasiswa/{id}`

**Headers**:
```
Authorization: Bearer <token>
```

**Example**:
```
DELETE http://127.0.0.1:8000/mahasiswa/16
```

**Response Success (200 OK)**:
```json
{
  "message": "Mahasiswa berhasil dihapus",
  "deleted_id": 16
}
```

**Response Error (404 Not Found)**:
```json
{
  "detail": "Mahasiswa tidak ditemukan"
}
```

---

## 📚 MATA KULIAH CRUD

### 1. CREATE Mata Kuliah (POST)

**Endpoint**: `POST http://127.0.0.1:8000/matakuliah`

**Headers**:
```
Authorization: Bearer <token>
Content-Type: application/json
```

**Request Body** (Semua field WAJIB):
```json
{
  "kode_mk": "KOM0009",
  "nama_mk": "Pemrograman Web",
  "sks": 3,
  "semester": 5
}
```

**Field Requirements**:
- `kode_mk` (string, required) - Kode mata kuliah, harus unique
- `nama_mk` (string, required) - Nama mata kuliah
- `sks` (integer, required) - Jumlah SKS (1-6)
- `semester` (integer, required) - Semester (1-8)

**Response Success (201 Created)**:
```json
{
  "message": "Mata kuliah berhasil ditambahkan",
  "data": {
    "kode_mk": "KOM0009",
    "nama_mk": "Pemrograman Web",
    "sks": 3,
    "semester": 5
  }
}
```

**Response Error (400 Bad Request)**:
```json
{
  "detail": "Kode mata kuliah sudah terdaftar"
}
```

---

### 2. GET All Mata Kuliah

**Endpoint**: `GET http://127.0.0.1:8000/matakuliah`

**Headers**:
```
Authorization: Bearer <token>
```

**Query Parameters** (Optional):
- `skip` (integer, default: 0)
- `limit` (integer, default: 100)

**Response Success (200 OK)**:
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

### 3. GET Mata Kuliah by Kode

**Endpoint**: `GET http://127.0.0.1:8000/matakuliah/{kode_mk}`

**Headers**:
```
Authorization: Bearer <token>
```

**Example**:
```
GET http://127.0.0.1:8000/matakuliah/KOM0001
```

**Response Success (200 OK)**:
```json
{
  "kode_mk": "KOM0001",
  "nama_mk": "Pemrograman Dasar",
  "sks": 3,
  "semester": 1
}
```

---

### 4. UPDATE Mata Kuliah (PUT)

**Endpoint**: `PUT http://127.0.0.1:8000/matakuliah/{kode_mk}`

**Headers**:
```
Authorization: Bearer <token>
Content-Type: application/json
```

**Request Body** (Semua field OPTIONAL):
```json
{
  "nama_mk": "Pemrograman Dasar (Updated)",
  "sks": 4,
  "semester": 1
}
```

**Example - Update hanya nama**:
```json
{
  "nama_mk": "Pemrograman Dasar Lanjut"
}
```

**Response Success (200 OK)**:
```json
{
  "message": "Mata kuliah berhasil diupdate",
  "data": {
    "kode_mk": "KOM0001",
    "nama_mk": "Pemrograman Dasar Lanjut",
    "sks": 3,
    "semester": 1
  }
}
```

---

### 5. DELETE Mata Kuliah

**Endpoint**: `DELETE http://127.0.0.1:8000/matakuliah/{kode_mk}`

**Headers**:
```
Authorization: Bearer <token>
```

**Example**:
```
DELETE http://127.0.0.1:8000/matakuliah/KOM0009
```

**Response Success (200 OK)**:
```json
{
  "message": "Mata kuliah berhasil dihapus",
  "deleted_kode": "KOM0009"
}
```

---

## 🔑 LOGIN

### POST Login

**Endpoint**: `POST http://127.0.0.1:8000/auth/login`

**Headers**:
```
Content-Type: application/json
```

**Request Body** (Semua field WAJIB):
```json
{
  "email": "dosen@absenin.local",
  "password": "dosen123"
}
```

**Response Success (200 OK)**:
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

**Response Error (401 Unauthorized)**:
```json
{
  "detail": "Email tidak ditemukan"
}
```
atau
```json
{
  "detail": "Password salah"
}
```

---

## 📋 Validation Rules

### Mahasiswa
- NIM: Harus unique, tidak boleh kosong
- Nama: Tidak boleh kosong
- Kelas: Tidak boleh kosong
- Prodi: Tidak boleh kosong

### Mata Kuliah
- Kode MK: Harus unique, tidak boleh kosong
- Nama MK: Tidak boleh kosong
- SKS: Harus integer, tidak boleh kosong
- Semester: Harus integer, tidak boleh kosong

---

## 🎯 Quick Test di Postman

### 1. Login
```
POST http://127.0.0.1:8000/auth/login
Body: {"email": "dosen@absenin.local", "password": "dosen123"}
→ Copy access_token
```

### 2. Create Mahasiswa
```
POST http://127.0.0.1:8000/mahasiswa
Authorization: Bearer <token>
Body: {
  "nim": "J0403231999",
  "nama": "TEST MAHASISWA",
  "kelas": "A",
  "prodi": "TRPL"
}
```

### 3. Get All Mahasiswa
```
GET http://127.0.0.1:8000/mahasiswa
Authorization: Bearer <token>
```

### 4. Update Mahasiswa
```
PUT http://127.0.0.1:8000/mahasiswa/18
Authorization: Bearer <token>
Body: {"nama": "TEST MAHASISWA UPDATED"}
```

### 5. Delete Mahasiswa
```
DELETE http://127.0.0.1:8000/mahasiswa/18
Authorization: Bearer <token>
```

---

## 🌐 Server Info

- **Base URL**: http://127.0.0.1:8000
- **API Docs**: http://127.0.0.1:8000/docs (Interactive!)
- **ReDoc**: http://127.0.0.1:8000/redoc

---

**Semua request sudah terdokumentasi lengkap dengan contoh!** 🎉
