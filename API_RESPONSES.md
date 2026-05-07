# 📝 API Response Messages - Complete Guide

## ✅ Response Format Baru

Semua operasi CRUD sekarang mengembalikan response message yang jelas!

---

## 📚 Mahasiswa Endpoints

### 1. CREATE Mahasiswa
**POST** `/mahasiswa`

**Request**:
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
  "message": "Mahasiswa berhasil ditambahkan",
  "data": {
    "nim": "J0403231999",
    "nama": "MAHASISWA BARU",
    "kelas": "A",
    "prodi": "TRPL",
    "id_mahasiswa": 18
  }
}
```

---

### 2. UPDATE Mahasiswa
**PUT** `/mahasiswa/{id}`

**Request**:
```json
{
  "nama": "MAHASISWA UPDATED",
  "kelas": "B"
}
```

**Response** (200 OK):
```json
{
  "message": "Mahasiswa berhasil diupdate",
  "data": {
    "nim": "J0403231999",
    "nama": "MAHASISWA UPDATED",
    "kelas": "B",
    "prodi": "TRPL",
    "id_mahasiswa": 18
  }
}
```

---

### 3. DELETE Mahasiswa
**DELETE** `/mahasiswa/{id}`

**Response** (200 OK):
```json
{
  "message": "Mahasiswa berhasil dihapus",
  "deleted_id": 18
}
```

---

## 📖 Mata Kuliah Endpoints

### 1. CREATE Mata Kuliah
**POST** `/matakuliah`

**Request**:
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
  "message": "Mata kuliah berhasil ditambahkan",
  "data": {
    "kode_mk": "KOM0009",
    "nama_mk": "Pemrograman Web",
    "sks": 3,
    "semester": 5
  }
}
```

---

### 2. UPDATE Mata Kuliah
**PUT** `/matakuliah/{kode_mk}`

**Request**:
```json
{
  "nama_mk": "Pemrograman Web Lanjut",
  "sks": 4
}
```

**Response** (200 OK):
```json
{
  "message": "Mata kuliah berhasil diupdate",
  "data": {
    "kode_mk": "KOM0009",
    "nama_mk": "Pemrograman Web Lanjut",
    "sks": 4,
    "semester": 5
  }
}
```

---

### 3. DELETE Mata Kuliah
**DELETE** `/matakuliah/{kode_mk}`

**Response** (200 OK):
```json
{
  "message": "Mata kuliah berhasil dihapus",
  "deleted_kode": "KOM0009"
}
```

---

## ❌ Error Responses

### 404 Not Found
```json
{
  "detail": "Mahasiswa tidak ditemukan"
}
```

### 400 Bad Request (Duplicate)
```json
{
  "detail": "NIM sudah terdaftar"
}
```

### 401 Unauthorized (No Token)
```json
{
  "detail": "Not authenticated"
}
```

---

## 🧪 Test di Postman

### CREATE Test
```
POST http://127.0.0.1:8000/mahasiswa
Authorization: Bearer <token>

Body:
{
  "nim": "J0403231999",
  "nama": "TEST MAHASISWA",
  "kelas": "A",
  "prodi": "TRPL"
}

Expected Response:
✅ 201 Created
{
  "message": "Mahasiswa berhasil ditambahkan",
  "data": { ... }
}
```

### UPDATE Test
```
PUT http://127.0.0.1:8000/mahasiswa/18
Authorization: Bearer <token>

Body:
{
  "nama": "TEST UPDATED"
}

Expected Response:
✅ 200 OK
{
  "message": "Mahasiswa berhasil diupdate",
  "data": { ... }
}
```

### DELETE Test
```
DELETE http://127.0.0.1:8000/mahasiswa/18
Authorization: Bearer <token>

Expected Response:
✅ 200 OK
{
  "message": "Mahasiswa berhasil dihapus",
  "deleted_id": 18
}
```

---

## 📊 Response Structure

### Success Response (Create/Update)
```typescript
{
  message: string,      // Success message
  data: Object | null   // Created/Updated object
}
```

### Success Response (Delete)
```typescript
{
  message: string,           // Success message
  deleted_id: number | null, // ID yang dihapus (mahasiswa)
  deleted_kode: string | null // Kode yang dihapus (matakuliah)
}
```

### Error Response
```typescript
{
  detail: string  // Error message
}
```

---

## 🎯 Summary

**Sebelum**:
- ❌ CREATE: Return data saja
- ❌ UPDATE: Return data saja
- ❌ DELETE: Return null (204 No Content)

**Sekarang**:
- ✅ CREATE: Return message + data
- ✅ UPDATE: Return message + data
- ✅ DELETE: Return message + deleted_id/kode

**Benefit**:
- ✅ Response lebih jelas
- ✅ Mudah di-handle di frontend
- ✅ Konsisten untuk semua endpoints
- ✅ User-friendly messages

---

**Server**: http://127.0.0.1:8000
**Docs**: http://127.0.0.1:8000/docs

**Semua CRUD operations sekarang memiliki response message yang jelas!** 🎉
