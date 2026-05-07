# 🔴 ERROR: Permission Denied - SOLUSI LENGKAP

## Error yang Terjadi

```
Error: [Errno 13] Permission denied: 
'D:\...\venv\Scripts\python.exe'
```

## Penyebab

Ada proses yang masih menggunakan file di folder `venv`, sehingga Windows tidak bisa menghapusnya.

---

## ✅ SOLUSI 1: Tutup Semua Proses (RECOMMENDED)

### Langkah 1: Tutup Aplikasi
Tutup SEMUA aplikasi berikut:
- ✅ Command Prompt / PowerShell (SEMUA window)
- ✅ VS Code / PyCharm / IDE lainnya
- ✅ File Explorer yang membuka folder project
- ✅ Git Bash / Terminal lainnya

### Langkah 2: Tutup Python Processes
1. Tekan `Ctrl + Shift + Esc` (buka Task Manager)
2. Cari proses dengan nama:
   - `python.exe`
   - `pythonw.exe`
   - `uvicorn.exe`
3. Klik kanan → End Task

### Langkah 3: Tunggu Sebentar
Tunggu 5-10 detik agar Windows melepas semua file handle.

### Langkah 4: Jalankan Setup Lagi
```bash
setup.bat
```

---

## ✅ SOLUSI 2: Hapus Manual

### Cara 1: File Explorer
1. Tutup semua aplikasi (lihat Solusi 1)
2. Buka File Explorer
3. Navigasi ke folder project
4. Klik kanan folder `venv`
5. Pilih **Delete**
6. Jika muncul error, tunggu 10 detik dan coba lagi
7. Jalankan `setup.bat`

### Cara 2: Gunakan Script Helper
```bash
delete_venv.bat
```

Script ini akan mencoba menghapus folder venv dengan berbagai metode.

---

## ✅ SOLUSI 3: Restart Komputer

Jika solusi 1 dan 2 tidak berhasil:

1. **Restart komputer**
2. Setelah restart, langsung jalankan:
```bash
setup.bat
```

---

## ✅ SOLUSI 4: Gunakan Safe Mode (Terakhir)

Jika masih gagal:

1. Restart komputer ke Safe Mode
2. Hapus folder `venv` secara manual
3. Restart normal
4. Jalankan `setup.bat`

---

## 🔍 Cara Cek Proses yang Menggunakan File

### Menggunakan Resource Monitor (Windows)

1. Tekan `Win + R`
2. Ketik: `resmon`
3. Tab **CPU**
4. Di kolom **Associated Handles**, ketik: `venv`
5. Lihat proses mana yang menggunakan file di folder venv
6. Tutup proses tersebut

### Menggunakan Command Line

```bash
# Cek proses Python yang berjalan
tasklist | findstr python

# Kill proses Python (ganti PID dengan nomor yang muncul)
taskkill /F /PID <PID>
```

---

## 🎯 Pencegahan

Untuk menghindari masalah ini di masa depan:

### 1. Selalu Deactivate Virtual Environment
```bash
# Sebelum menutup terminal
deactivate
```

### 2. Tutup Server dengan Benar
```bash
# Tekan Ctrl+C untuk stop server
# Tunggu sampai proses benar-benar berhenti
```

### 3. Tutup IDE dengan Benar
- Jangan force close VS Code
- Gunakan File → Exit

### 4. Jangan Buka Banyak Terminal
- Gunakan satu terminal untuk development
- Tutup terminal yang tidak digunakan

---

## 📋 Checklist Troubleshooting

Coba langkah-langkah ini secara berurutan:

- [ ] Tutup semua Command Prompt / PowerShell
- [ ] Tutup VS Code / IDE
- [ ] Tutup File Explorer
- [ ] End Task semua proses Python di Task Manager
- [ ] Tunggu 10 detik
- [ ] Jalankan `setup.bat`

Jika masih gagal:

- [ ] Jalankan `delete_venv.bat`
- [ ] Tunggu 10 detik
- [ ] Jalankan `setup.bat`

Jika masih gagal:

- [ ] Hapus folder `venv` manual di File Explorer
- [ ] Tunggu 10 detik
- [ ] Jalankan `setup.bat`

Jika masih gagal:

- [ ] Restart komputer
- [ ] Jalankan `setup.bat`

---

## 💡 Tips

### Jika Sering Terjadi

Buat script untuk kill semua proses Python sebelum setup:

```batch
@echo off
echo Menghentikan semua proses Python...
taskkill /F /IM python.exe 2>nul
taskkill /F /IM pythonw.exe 2>nul
timeout /t 2 /nobreak >nul
echo Selesai.
pause
```

Simpan sebagai `kill_python.bat` dan jalankan sebelum `setup.bat`.

---

## 🆘 Masih Gagal?

Jika semua solusi di atas tidak berhasil:

1. **Cek Antivirus**
   - Antivirus mungkin mengunci file
   - Tambahkan folder project ke whitelist
   - Atau disable sementara

2. **Cek Permissions**
   - Klik kanan folder project
   - Properties → Security
   - Pastikan user Anda punya Full Control

3. **Gunakan Folder Lain**
   - Copy project ke folder lain (misal: `C:\Projects\`)
   - Jalankan `setup.bat` di folder baru

4. **Reinstall Python**
   - Uninstall Python
   - Restart komputer
   - Install Python lagi
   - Jalankan `setup.bat`

---

## 📞 Bantuan Lebih Lanjut

Jika masih ada masalah, buat issue di repository dengan informasi:
- Error message lengkap
- Screenshot Task Manager (proses Python)
- Langkah yang sudah dicoba
- Versi Windows dan Python

---

**Ingat**: Masalah ini BUKAN karena code error, tapi karena Windows file locking. Solusinya adalah memastikan tidak ada proses yang menggunakan file di folder venv.
