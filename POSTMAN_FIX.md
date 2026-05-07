# 🔍 Troubleshooting JWT Token di Postman

## ❌ Masalah yang Terjadi

Dari log server:
```
POST /auth/login → 200 OK ✅ (Login berhasil)
DELETE /mahasiswa/17 → 401 Unauthorized ❌ (Token tidak dikirim)
GET /mahasiswa → 307 Temporary Redirect → GET /mahasiswa/ → 401 Unauthorized ❌
```

**Kesimpulan**: Token tidak dikirim atau format salah di Postman!

---

## ✅ Solusi Step-by-Step

### Step 1: Verifikasi Token Valid

**Test dengan curl/Python** (sudah berhasil):
- ✅ Endpoint `/mahasiswa` dengan token → 200 OK
- ✅ JWT token valid dan berfungsi

**Masalah di Postman**:
- ❌ Authorization header tidak dikirim dengan benar

---

### Step 2: Perbaiki Setup di Postman

#### Cara 1: Authorization Tab (RECOMMENDED)

1. **Buat Request Baru**:
   ```
   GET http://127.0.0.1:8000/mahasiswa
   ```

2. **Klik Tab "Authorization"**

3. **Pilih Type**:
   - Dropdown: **"Bearer Token"**

4. **Paste Token**:
   ```
   eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZXhwIjoxNzc4MTY5NDM2fQ.8CSUxUXu_9qRJuBc1AnzEG9t5HZFs5uWahsntBOtdIQ
   ```

5. **Jangan tambah "Bearer"** - Postman otomatis tambahkan!

6. **Klik Send** → Harus dapat 200 OK ✅

---

#### Cara 2: Manual Header (Alternative)

1. **Tab "Headers"**

2. **Add Header**:
   - Key: `Authorization`
   - Value: `Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZXhwIjoxNzc4MTY5NDM2fQ.8CSUxUXu_9qRJuBc1AnzEG9t5HZFs5uWahsntBOtdIQ`

3. **Pastikan ada spasi** setelah "Bearer"

4. **Klik Send** → Harus dapat 200 OK ✅

---

### Step 3: Troubleshooting Common Issues

#### Issue: "Token expired" (401)
**Solusi**: Login ulang untuk dapat token baru
```
POST /auth/login
Body: {"email": "dosen@absenin.local", "password": "dosen123"}
```

#### Issue: "Not authenticated" (401)
**Penyebab**: Authorization header tidak ada
**Solusi**: Pastikan tab Authorization sudah diset dengan benar

#### Issue: "Token tidak valid" (401)
**Penyebab**: Token malformed atau corrupt
**Solusi**: Copy ulang token dari response login

---

### Step 4: Test Semua Endpoints

#### ✅ Test Berhasil (200 OK)

**GET Mahasiswa**:
```
GET /mahasiswa
Authorization: Bearer <token>
```

**GET Mata Kuliah**:
```
GET /matakuliah
Authorization: Bearer <token>
```

**POST Mahasiswa Baru**:
```
POST /mahasiswa
Authorization: Bearer <token>
Body: {
  "nim": "J0403232000",
  "nama": "TEST MAHASISWA",
  "kelas": "A",
  "prodi": "TRPL"
}
```

**POST Mata Kuliah Baru**:
```
POST /matakuliah
Authorization: Bearer <token>
Body: {
  "kode_mk": "TEST001",
  "nama_mk": "Test Mata Kuliah",
  "sks": 3,
  "semester": 1
}
```

#### ❌ Test Gagal (401 Unauthorized)

**Tanpa Authorization Header**:
```
GET /mahasiswa
(tanpa header Authorization)
```

---

## 🔧 Tips Postman

### 1. Save Request ke Collection
- Klik "Save" setelah buat request
- Buat collection: "AbsenIN API Tests"
- Organize by folder: Auth, Mahasiswa, Mata Kuliah

### 2. Use Environment Variables
1. Klik ikon ⚙️ → Environments
2. Add: "AbsenIN Local"
3. Variable: `token` (kosong)
4. Set via Tests tab setelah login:
   ```javascript
   pm.environment.set("token", pm.response.json().access_token);
   ```
5. Use: `{{token}}` di Authorization tab

### 3. Check Headers
Klik tab "Headers" untuk verifikasi header Authorization dikirim dengan benar.

### 4. Clear Cache
Jika masih error, clear cache Postman atau restart Postman.

---

## 📊 Expected Responses

### Login Success (200)
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "user": {
    "email": "dosen@absenin.local",
    "name": "Dosen",
    "id": 1
  }
}
```

### Protected Endpoint Success (200)
```json
[
  {
    "id_mahasiswa": 1,
    "nim": "J0403231006",
    "nama": "AZZAHRA NABILA CHAIRONA",
    "kelas": "A",
    "prodi": "TRPL"
  }
]
```

### Unauthorized (401)
```json
{
  "detail": "Not authenticated"
}
```

---

## 🎯 Checklist

- [ ] Login berhasil (200 OK)
- [ ] Copy token dari response
- [ ] Set Authorization header di Postman
- [ ] GET /mahasiswa berhasil (200 OK)
- [ ] GET /matakuliah berhasil (200 OK)
- [ ] POST /mahasiswa berhasil (201 Created)
- [ ] POST /matakuliah berhasil (201 Created)

---

## 💡 Kesimpulan

**Masalah**: Postman tidak mengirim Authorization header dengan benar

**Solusi**: 
1. ✅ Pastikan menggunakan "Bearer Token" type di tab Authorization
2. ✅ Atau manual header: `Authorization: Bearer <token>`
3. ✅ Copy token yang benar dari response login

**Status**: Endpoint backend sudah berfungsi 100%! Masalah hanya di setup Postman.

---

**Coba lagi dengan setup yang benar di atas!** 🚀
