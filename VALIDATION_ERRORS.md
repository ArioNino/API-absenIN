# 📋 Validation Error Messages - API AbsenIN

## ✅ Validasi Sudah Aktif!

API sekarang memberikan pesan error yang jelas tentang field apa saja yang wajib diisi.

---

## 🎓 MAHASISWA - Validation Rules

### Required Fields
Semua field wajib diisi:
- `nim` (string, min 1 karakter, max 11 karakter)
- `nama` (string, min 1 karakter)
- `kelas` (string, min 1 karakter)
- `prodi` (string, min 1 karakter)

### Error Examples

#### 1. Request Kosong
**Request**:
```json
{}
```

**Response (422 Unprocessable Entity)**:
```json
{
  "detail": [
    {
      "type": "missing",
      "loc": ["body", "nim"],
      "msg": "Field required",
      "input": {}
    },
    {
      "type": "missing",
      "loc": ["body", "nama"],
      "msg": "Field required",
      "input": {}
    },
    {
      "type": "missing",
      "loc": ["body", "kelas"],
      "msg": "Field required",
      "input": {}
    },
    {
      "type": "missing",
      "loc": ["body", "prodi"],
      "msg": "Field required",
      "input": {}
    }
  ]
}
```

**Artinya**: Semua field (nim, nama, kelas, prodi) wajib diisi!

---

#### 2. Field Tidak Lengkap
**Request**:
```json
{
  "nim": "J0403231999"
}
```

**Response (422)**:
```json
{
  "detail": [
    {
      "type": "missing",
      "loc": ["body", "nama"],
      "msg": "Field required"
    },
    {
      "type": "missing",
      "loc": ["body", "kelas"],
      "msg": "Field required"
    },
    {
      "type": "missing",
      "loc": ["body", "prodi"],
      "msg": "Field required"
    }
  ]
}
```

**Artinya**: Field nama, kelas, dan prodi masih kosong!

---

#### 3. Field Kosong (Empty String)
**Request**:
```json
{
  "nim": "",
  "nama": "Test",
  "kelas": "A",
  "prodi": "TRPL"
}
```

**Response (422)**:
```json
{
  "detail": [
    {
      "type": "string_too_short",
      "loc": ["body", "nim"],
      "msg": "String should have at least 1 character",
      "input": ""
    }
  ]
}
```

**Artinya**: NIM tidak boleh kosong!

---

#### 4. NIM Terlalu Panjang
**Request**:
```json
{
  "nim": "J040323199999999",
  "nama": "Test",
  "kelas": "A",
  "prodi": "TRPL"
}
```

**Response (422)**:
```json
{
  "detail": [
    {
      "type": "string_too_long",
      "loc": ["body", "nim"],
      "msg": "String should have at most 11 characters",
      "input": "J040323199999999"
    }
  ]
}
```

**Artinya**: NIM maksimal 11 karakter!

---

## 📚 MATA KULIAH - Validation Rules

### Required Fields
Semua field wajib diisi:
- `kode_mk` (string, min 1 karakter, max 10 karakter)
- `nama_mk` (string, min 1 karakter)
- `sks` (integer, min 1, max 6)
- `semester` (integer, min 1, max 8)

### Error Examples

#### 1. SKS Invalid (Lebih dari 6)
**Request**:
```json
{
  "kode_mk": "KOM9999",
  "nama_mk": "Test",
  "sks": 10,
  "semester": 1
}
```

**Response (422)**:
```json
{
  "detail": [
    {
      "type": "less_than_equal",
      "loc": ["body", "sks"],
      "msg": "Input should be less than or equal to 6",
      "input": 10,
      "ctx": {"le": 6}
    }
  ]
}
```

**Artinya**: SKS maksimal 6!

---

#### 2. Semester Invalid (Lebih dari 8)
**Request**:
```json
{
  "kode_mk": "KOM9999",
  "nama_mk": "Test",
  "sks": 3,
  "semester": 10
}
```

**Response (422)**:
```json
{
  "detail": [
    {
      "type": "less_than_equal",
      "loc": ["body", "semester"],
      "msg": "Input should be less than or equal to 8",
      "input": 10,
      "ctx": {"le": 8}
    }
  ]
}
```

**Artinya**: Semester maksimal 8!

---

#### 3. SKS Negatif atau 0
**Request**:
```json
{
  "kode_mk": "KOM9999",
  "nama_mk": "Test",
  "sks": 0,
  "semester": 1
}
```

**Response (422)**:
```json
{
  "detail": [
    {
      "type": "greater_than_equal",
      "loc": ["body", "sks"],
      "msg": "Input should be greater than or equal to 1",
      "input": 0,
      "ctx": {"ge": 1}
    }
  ]
}
```

**Artinya**: SKS minimal 1!

---

## ✅ Request Valid

### Mahasiswa
**Request**:
```json
{
  "nim": "J0403231888",
  "nama": "TEST MAHASISWA",
  "kelas": "A",
  "prodi": "TRPL"
}
```

**Response (201 Created)**:
```json
{
  "message": "Mahasiswa berhasil ditambahkan",
  "data": {
    "id_mahasiswa": 22,
    "nim": "J0403231888",
    "nama": "TEST MAHASISWA",
    "kelas": "A",
    "prodi": "TRPL"
  }
}
```

---

### Mata Kuliah
**Request**:
```json
{
  "kode_mk": "KOM0009",
  "nama_mk": "Pemrograman Web",
  "sks": 3,
  "semester": 5
}
```

**Response (201 Created)**:
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

## 📊 Summary Error Codes

| Status Code | Meaning | Kapan Terjadi |
|-------------|---------|---------------|
| **422** | Unprocessable Entity | Validasi gagal (field kosong, format salah, dll) |
| **400** | Bad Request | NIM/Kode MK sudah terdaftar |
| **401** | Unauthorized | Token tidak valid atau expired |
| **404** | Not Found | Data tidak ditemukan |
| **201** | Created | Data berhasil dibuat |
| **200** | OK | Request berhasil |

---

## 💡 Tips

1. ✅ **Baca error message** - Pydantic memberikan detail field mana yang error
2. ✅ **Cek `loc`** - Menunjukkan lokasi error (body, nim, nama, dll)
3. ✅ **Cek `msg`** - Pesan error dalam bahasa Inggris
4. ✅ **Cek `type`** - Tipe error (missing, string_too_short, dll)
5. ✅ **Test di Swagger UI** - http://127.0.0.1:8000/docs untuk test interaktif

---

**Server**: http://127.0.0.1:8000
**Docs**: http://127.0.0.1:8000/docs

**Validasi sudah aktif! API sekarang memberikan pesan error yang jelas.** ✅
