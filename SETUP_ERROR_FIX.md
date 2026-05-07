# ⚠️ PENTING - Jika Setup Gagal

## Error: "Could not open requirements file"

Jika Anda mendapat error:
```
ERROR: Could not open requirements file: [Errno 2] No such file or directory: 'requirements.txt'
```

### Penyebab
Script tidak berjalan dari direktori yang benar.

### Solusi

#### Cara 1: Jalankan dari File Explorer (RECOMMENDED)
1. Buka folder project di File Explorer
2. Double-click file `setup.bat`
3. Script akan otomatis berjalan dari direktori yang benar

#### Cara 2: Jalankan dari Command Prompt
```bash
# Pindah ke direktori project
cd "D:\kulyeahhh\sem6\Visual Komputer Cerdas\project\API-absenIN"

# Jalankan setup
setup.bat
```

#### Cara 3: Drag & Drop
1. Buka Command Prompt
2. Ketik: `cd ` (dengan spasi di akhir)
3. Drag folder project ke Command Prompt
4. Tekan Enter
5. Ketik: `setup.bat`

### Verifikasi
Setelah script berjalan, Anda akan melihat:
```
Working directory: D:\kulyeahhh\sem6\Visual Komputer Cerdas\project\API-absenIN
```

Jika path sudah benar, setup akan berjalan lancar.

---

## Error Lainnya

### "Python tidak ditemukan"
**Solusi**: Install Python dari https://www.python.org/

### "Gagal menginstall dependencies"
**Solusi**: 
1. Pastikan koneksi internet aktif
2. Coba manual:
```bash
venv\Scripts\activate
pip install -r requirements.txt
```

### "Virtual environment tidak ditemukan"
**Solusi**: Jalankan `setup.bat` terlebih dahulu

---

## Cara Benar Menjalankan Script

### ✅ BENAR
```bash
# Dari folder project
D:\...\API-absenIN> setup.bat
```

### ❌ SALAH
```bash
# Dari folder lain
D:\> setup.bat
D:\> D:\...\API-absenIN\setup.bat
```

---

## Tips

1. **Selalu jalankan script dari folder project**
2. **Gunakan File Explorer untuk double-click** (paling mudah)
3. **Atau gunakan `cd` untuk pindah ke folder project dulu**

---

Lihat `TROUBLESHOOTING.md` untuk solusi lengkap masalah lainnya.
