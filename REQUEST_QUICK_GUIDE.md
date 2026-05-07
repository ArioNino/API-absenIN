# 📋 Quick Reference - Request Body untuk CRUD

## 🎓 MAHASISWA

### CREATE (POST /mahasiswa)
**Required Fields** (Semua wajib diisi):
```json
{
  "nim": "J0403231999",
  "nama": "NAMA LENGKAP MAHASISWA",
  "kelas": "A",
  "prodi": "TRPL"
}
```

### UPDATE (PUT /mahasiswa/{id})
**Optional Fields** (Isi yang ingin diubah saja):
```json
{
  "nim": "J0403231999",
  "nama": "NAMA BARU",
  "kelas": "B",
  "prodi": "JMP"
}
```

---

## 📚 MATA KULIAH

### CREATE (POST /matakuliah)
**Required Fields** (Semua wajib diisi):
```json
{
  "kode_mk": "KOM0009",
  "nama_mk": "Pemrograman Web",
  "sks": 3,
  "semester": 5
}
```

### UPDATE (PUT /matakuliah/{kode_mk})
**Optional Fields** (Isi yang ingin diubah saja):
```json
{
  "nama_mk": "Pemrograman Web Lanjut",
  "sks": 4,
  "semester": 6
}
```

---

## 🔑 Field Descriptions

### Mahasiswa
- **nim**: NIM mahasiswa (11 karakter, unique)
- **nama**: Nama lengkap mahasiswa
- **kelas**: Kelas (A, B, C, dll)
- **prodi**: Program studi (TRPL, JMP, dll)

### Mata Kuliah
- **kode_mk**: Kode mata kuliah (max 10 karakter, unique)
- **nama_mk**: Nama mata kuliah
- **sks**: Jumlah SKS (integer)
- **semester**: Semester (integer)

---

## ⚠️ Validasi

### CREATE
- ✅ Semua field wajib diisi
- ✅ NIM/Kode MK harus unique
- ❌ Tidak boleh ada field kosong

### UPDATE
- ✅ Minimal 1 field diisi
- ✅ Field yang tidak diisi tidak akan berubah
- ✅ NIM/Kode MK bisa diubah (jika unique)

---

**Lihat dokumentasi lengkap**: `API_REQUEST_GUIDE.md`

**Server**: http://127.0.0.1:8000
**Docs**: http://127.0.0.1:8000/docs
