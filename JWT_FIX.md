# Test JWT Token Fix

## Problem
Token lama error karena 'sub' adalah integer, tapi PyJWT mengharapkan string.

## Solution
1. ✅ Update auth.py: convert user.id to str(user.id) saat create token
2. ✅ Update auth.py: convert sub dari string ke int saat decode token

## Test Login Baru

Mari test login untuk dapat token baru:

POST http://127.0.0.1:8000/auth/login
Body:
```json
{
  "email": "dosen@absenin.local",
  "password": "dosen123"
}
```

Expected Response:
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

Perhatikan: "sub":"1" (string) bukan "sub":1 (integer)

## Test Token di Postman

1. Login untuk dapat token baru
2. Copy access_token
3. Test endpoint protected:
   GET http://127.0.0.1:8000/mahasiswa
   Authorization: Bearer <token>

Expected: 200 OK dengan list mahasiswa

---

**Server sudah restart dengan JWT fix!** 🎉