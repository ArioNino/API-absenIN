# 🔄 Update Operations - Dirty Check Implementation

## ✅ Fitur Baru: Dirty Check

Sekarang operasi UPDATE memiliki validasi "dirty check" yang memastikan:
1. ✅ Minimal 1 field harus diubah
2. ✅ Tidak bisa update tanpa perubahan data
3. ✅ Error message yang jelas jika tidak ada perubahan

---

## 📋 Cara Kerja

### UPDATE Mahasiswa

**Endpoint**: `PUT /mahasiswa/{id}`

**Request Body** (minimal 1 field):
```json
{
  "nama": "NAMA BARU"
}
```

**Validasi**:
- ✅ Minimal 1 field harus diisi
- ✅ Field yang tidak diisi tidak akan berubah
- ✅ Jika semua field kosong → Error 400

---

## 🧪 Test Cases

### ✅ Test 1: Update dengan 1 Field (BERHASIL)
```
PUT http://127.0.0.1:8000/mahasiswa/1
Authorization: Bearer <token>

Body:
{
  "nama": "AZZAHRA NABILA (UPDATED)"
}

Response: 200 OK
{
  "message": "Mahasiswa berhasil diupdate",
  "data": {
    "id_mahasiswa": 1,
    "nim": "J0403231006",
    "nama": "AZZAHRA NABILA (UPDATED)",
    "kelas": "A",
    "prodi": "TRPL"
  }
}
```

### ✅ Test 2: Update dengan Multiple Fields (BERHASIL)
```
PUT http://127.0.0.1:8000/mahasiswa/1
Authorization: Bearer <token>

Body:
{
  "nama": "AZZAHRA NABILA",
  "kelas": "B"
}

Response: 200 OK
{
  "message": "Mahasiswa berhasil diupdate",
  "data": { ... }
}
```

### ❌ Test 3: Update dengan Body Kosong (ERROR)
```
PUT http://127.0.0.1:8000/mahasiswa/1
Authorization: Bearer <token>

Body:
{}

Response: 400 Bad Request
{
  "detail": "Tidak ada data yang diupdate. Minimal 1 field harus diisi."
}
```

### ❌ Test 4: Update dengan Semua Field Null (ERROR)
```
PUT http://127.0.0.1:8000/mahasiswa/1
Authorization: Bearer <token>

Body:
{
  "nim": null,
  "nama": null,
  "kelas": null,
  "prodi": null
}

Response: 400 Bad Request
{
  "detail": "Tidak ada data yang diupdate. Minimal 1 field harus diisi."
}
```

---

## 📚 Update Mata Kuliah

**Endpoint**: `PUT /matakuliah/{kode_mk}`

### ✅ Update Berhasil
```
PUT http://127.0.0.1:8000/matakuliah/KOM0001
Authorization: Bearer <token>

Body:
{
  "nama_mk": "Pemrograman Dasar (Updated)",
  "sks": 4
}

Response: 200 OK
{
  "message": "Mata kuliah berhasil diupdate",
  "data": {
    "kode_mk": "KOM0001",
    "nama_mk": "Pemrograman Dasar (Updated)",
    "sks": 4,
    "semester": 1
  }
}
```

### ❌ Update Kosong (ERROR)
```
PUT http://127.0.0.1:8000/matakuliah/KOM0001
Authorization: Bearer <token>

Body:
{}

Response: 400 Bad Request
{
  "detail": "Tidak ada data yang diupdate. Minimal 1 field harus diisi."
}
```

---

## 💡 Tips

1. **Partial Update**: Anda hanya perlu mengirim field yang ingin diubah
2. **Field Validation**: Field yang dikirim tetap divalidasi (min/max length, range, dll)
3. **Dirty Check**: Sistem akan cek apakah ada perubahan data
4. **Error Clear**: Error message jelas jika tidak ada data yang diupdate

---

## 🎯 Error Messages

| Kondisi | Status | Message |
|---------|--------|---------|
| Body kosong | 400 | "Tidak ada data yang diupdate. Minimal 1 field harus diisi." |
| Semua field null | 400 | "Tidak ada data yang diupdate. Minimal 1 field harus diisi." |
| Field valid | 200 | "Mahasiswa berhasil diupdate" |
| NIM duplicate | 400 | "NIM sudah terdaftar" |
| ID tidak ada | 404 | "Mahasiswa tidak ditemukan" |

---

## 📖 Dokumentasi Terkait

- `API_REQUEST_GUIDE.md` - Request body lengkap
- `VALIDATION_ERRORS.md` - Error messages
- `CRUD_RESPONSES.md` - Response format

---

**Server**: http://127.0.0.1:8000
**Docs**: http://127.0.0.1:8000/docs

**Update operations sekarang dengan dirty check untuk memastikan ada perubahan data!** ✅
