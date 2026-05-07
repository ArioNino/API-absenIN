# 🧪 Testing API dengan Postman

## 📥 Setup Postman

1. Download Postman: https://www.postman.com/downloads/
2. Install dan buka Postman
3. Pastikan server API sudah berjalan di http://127.0.0.1:8000

## 🔐 Test Login Endpoint

### Endpoint Details
- **Method**: POST
- **URL**: `http://127.0.0.1:8000/auth/login`
- **Content-Type**: application/json

### Test Credentials

| Email | Password | Role |
|-------|----------|------|
| admin@absenin.local | admin123 | admin |
| dosen@absenin.local | dosen123 | dosen |
| mahasiswa@absenin.local | mahasiswa123 | mahasiswa |

---

## 📝 Langkah-langkah Testing di Postman

### 1. Test Login - Admin

**Step 1**: Buat Request Baru
- Klik "New" → "HTTP Request"
- Atau tekan `Ctrl + N`

**Step 2**: Set Method dan URL
- Method: `POST`
- URL: `http://127.0.0.1:8000/auth/login`

**Step 3**: Set Headers
- Tab "Headers"
- Add header:
  - Key: `Content-Type`
  - Value: `application/json`

**Step 4**: Set Body
- Tab "Body"
- Pilih "raw"
- Pilih "JSON" dari dropdown
- Masukkan:

```json
{
  "email": "admin@absenin.local",
  "password": "admin123"
}
```

**Step 5**: Send Request
- Klik tombol "Send"

**Expected Response** (200 OK):
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

---

### 2. Test Login - Dosen

**Body**:
```json
{
  "email": "dosen@absenin.local",
  "password": "dosen123"
}
```

**Expected Response**:
```json
{
  "status": "success",
  "message": "Login berhasil",
  "token": "dummy_token_2_dosen@absenin.local",
  "user": {
    "id": 2,
    "email": "dosen@absenin.local",
    "name": "Dosen Test",
    "role": "dosen"
  }
}
```

---

### 3. Test Login - Mahasiswa

**Body**:
```json
{
  "email": "mahasiswa@absenin.local",
  "password": "mahasiswa123"
}
```

**Expected Response**:
```json
{
  "status": "success",
  "message": "Login berhasil",
  "token": "dummy_token_3_mahasiswa@absenin.local",
  "user": {
    "id": 3,
    "email": "mahasiswa@absenin.local",
    "name": "Mahasiswa Test",
    "role": "mahasiswa"
  }
}
```

---

### 4. Test Login - Email Salah

**Body**:
```json
{
  "email": "wrong@email.com",
  "password": "admin123"
}
```

**Expected Response** (401 Unauthorized):
```json
{
  "detail": "Email tidak ditemukan"
}
```

---

### 5. Test Login - Password Salah

**Body**:
```json
{
  "email": "admin@absenin.local",
  "password": "wrongpassword"
}
```

**Expected Response** (401 Unauthorized):
```json
{
  "detail": "Password salah"
}
```

---

## 📋 Test Endpoints Lainnya

### Get All Mahasiswa

**Method**: GET
**URL**: `http://127.0.0.1:8000/mahasiswa`

**Response**:
```json
{
  "status": "success",
  "total": 5,
  "data": [
    {
      "id": 1,
      "nim": "J0403231006",
      "nama": "AZZAHRA NABILA CHAIRONA",
      "kelas": "A",
      "prodi": "TRPL"
    },
    ...
  ]
}
```

---

### Get Mahasiswa by ID

**Method**: GET
**URL**: `http://127.0.0.1:8000/mahasiswa/1`

**Response**:
```json
{
  "status": "success",
  "data": {
    "id": 1,
    "nim": "J0403231006",
    "nama": "AZZAHRA NABILA CHAIRONA",
    "kelas": "A",
    "prodi": "TRPL"
  }
}
```

---

### Get Mahasiswa by NIM

**Method**: GET
**URL**: `http://127.0.0.1:8000/mahasiswa/nim/J0403231006`

---

### Get All Kehadiran

**Method**: GET
**URL**: `http://127.0.0.1:8000/kehadiran`

**Response**:
```json
{
  "status": "success",
  "total": 5,
  "data": [
    {
      "id": 1,
      "mahasiswa_id": 1,
      "tanggal": "2026-05-07",
      "status": "Hadir",
      "keterangan": "Tepat waktu",
      "mahasiswa": {
        "id": 1,
        "nim": "J0403231006",
        "nama": "AZZAHRA NABILA CHAIRONA",
        "kelas": "A",
        "prodi": "TRPL"
      }
    },
    ...
  ]
}
```

---

### Get Statistics

**Method**: GET
**URL**: `http://127.0.0.1:8000/stats`

**Response**:
```json
{
  "status": "success",
  "data": {
    "total_mahasiswa": 5,
    "total_kehadiran": 5,
    "kehadiran_stats": {
      "hadir": 3,
      "izin": 1,
      "alpha": 1
    },
    "persentase_kehadiran": "60.0%"
  }
}
```

---

## 💾 Save Collection di Postman

### Cara Menyimpan Collection

1. Klik "Save" setelah membuat request
2. Beri nama: "AbsenIN API Tests"
3. Buat folder untuk organize:
   - Authentication
   - Mahasiswa
   - Kehadiran
   - Statistics

### Import/Export Collection

**Export**:
1. Klik "..." di collection
2. Pilih "Export"
3. Save as JSON

**Import**:
1. Klik "Import"
2. Pilih file JSON
3. Collection akan muncul

---

## 🔧 Tips Postman

### 1. Environment Variables

Buat environment untuk base URL:
- Variable: `base_url`
- Value: `http://127.0.0.1:8000`

Gunakan di URL: `{{base_url}}/auth/login`

### 2. Save Token

Setelah login, save token ke variable:
```javascript
// Tab "Tests" di request login
pm.test("Login successful", function () {
    var jsonData = pm.response.json();
    pm.environment.set("token", jsonData.token);
});
```

### 3. Pre-request Script

Auto set headers:
```javascript
pm.request.headers.add({
    key: 'Content-Type',
    value: 'application/json'
});
```

---

## 📸 Screenshot Guide

### Request Setup
```
Method: [POST ▼]  URL: http://127.0.0.1:8000/auth/login  [Send]

Headers | Body | Pre-request Script | Tests | Settings

Body:
  ○ none
  ○ form-data
  ○ x-www-form-urlencoded
  ● raw        [JSON ▼]

{
  "email": "admin@absenin.local",
  "password": "admin123"
}
```

### Response
```
Status: 200 OK    Time: 45 ms    Size: 234 B

Body | Cookies | Headers | Test Results

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

---

## ✅ Checklist Testing

- [ ] Login dengan admin berhasil
- [ ] Login dengan dosen berhasil
- [ ] Login dengan mahasiswa berhasil
- [ ] Login dengan email salah (401)
- [ ] Login dengan password salah (401)
- [ ] Get all mahasiswa
- [ ] Get mahasiswa by ID
- [ ] Get mahasiswa by NIM
- [ ] Get all kehadiran
- [ ] Get statistics

---

## 🐛 Troubleshooting

### Error: "Could not get any response"
- Pastikan server berjalan di http://127.0.0.1:8000
- Cek dengan browser: http://127.0.0.1:8000

### Error: "404 Not Found"
- Cek URL sudah benar
- Pastikan endpoint ada di http://127.0.0.1:8000/docs

### Error: "422 Unprocessable Entity"
- Cek format JSON sudah benar
- Pastikan field email dan password ada

---

## 📚 Resources

- **API Docs**: http://127.0.0.1:8000/docs
- **Postman Docs**: https://learning.postman.com/
- **FastAPI Docs**: https://fastapi.tiangolo.com/

---

**Happy Testing!** 🚀
