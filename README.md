# Dashboard Pelaporan Usulan Uji Kompetensi BKN

Dashboard interaktif untuk visualisasi dan analisis data usulan uji kompetensi TW III.

## 🚀 Fitur

- 📊 **Visualisasi Data Interaktif** - Diagram yang dinamis dan menarik
- 📁 **Upload CSV** - Upload file CSV langsung dari browser
- 🔍 **Filter Bulan** - Filter data berdasarkan bulan pengajuan
- 📈 **Multiple Charts**:
  - Diagram Usulan Per Bulan (Bar Chart)
  - Diagram Jenis Kenaikan Jabatan (Horizontal Bar Chart)
  - Diagram Jenis Jabatan Fungsional (Horizontal Bar Chart)
  - Diagram Status Progres Pengajuan (Doughnut Chart)
  - Diagram Status Kelulusan (Pie Chart)
- 📱 **Responsive Design** - Tampil optimal di desktop dan mobile
- 🎨 **Modern UI** - Desain dengan gradient dan animasi

## 🌐 Demo Online

Akses dashboard di: **https://iqbalcaraka.github.io/pendataan-ukom-bkn/dashboard.html**

> **Catatan**: Setelah GitHub Pages aktif, tunggu 1-2 menit untuk deployment pertama kali.

## 💻 Cara Menggunakan

### Online (GitHub Pages)
1. Buka link: https://iqbalcaraka.github.io/pendataan-ukom-bkn/dashboard.html
2. Klik tombol "📁 Pilih File CSV"
3. Pilih file `Pelaporan Pengolahan TWIII.csv`
4. Klik tombol "🚀 Load Data"
5. Dashboard akan menampilkan semua diagram dan statistik
6. Gunakan checkbox filter bulan untuk melihat data bulan tertentu

### Offline (Local)
1. Download file `dashboard.html`
2. Buka file dengan browser (Chrome, Firefox, Edge, dll)
3. Upload file CSV yang ingin dianalisis
4. Dashboard akan langsung berfungsi

## 📦 File Python Script

File `update_bulan_pengajuan.py` digunakan untuk:
- Normalisasi format tanggal di kolom "TANGGAL EMAIL MASUK"
- Konversi tanggal menjadi nama bulan Indonesia di kolom "BULAN PENGAJUAN"

### Cara Menggunakan Script Python:
```bash
python update_bulan_pengajuan.py
```

Script akan otomatis membaca dan mengupdate file CSV.

## 🛠️ Teknologi

- **HTML5** - Struktur aplikasi
- **CSS3** - Styling dengan gradient dan animasi
- **JavaScript** - Logika aplikasi
- **Chart.js** - Library untuk membuat diagram
- **PapaParse** - Library untuk parsing CSV
- **Python 3** - Script untuk processing data

## 📋 Format Data CSV

Dashboard mendukung CSV dengan kolom minimal:
- `NAMA` - Nama pegawai
- `BULAN PENGAJUAN` - Bulan pengajuan (Januari, Februari, dst)
- `TANGGAL EMAIL MASUK` - Tanggal email masuk
- `PROGRES PENGAJUAN` - Status progres (Selesai, Pengajuan Dari Unit, Usul Ujian)
- `STATUS KELULUSAN` - Status kelulusan (Lulus, Tidak Lulus, Proses)
- `KENAIKAN JENJANG JABATAN/ALIH JABATAN/PERPINDAHAN JABATAN` - Jenis kenaikan
- `JENIS JABATAN FUNGSIONAL` - Jenis jabatan fungsional

## 🎯 Roadmap

- [ ] Export diagram ke PDF
- [ ] Export data ke Excel
- [ ] Filter tambahan (unit kerja, jenis ujikom)
- [ ] Perbandingan data antar periode
- [ ] Dark mode

## 📄 Lisensi

Project ini dibuat untuk keperluan internal BKN.

## 👨‍💻 Developer

Dibuat dengan ❤️ menggunakan Claude Code

---

🤖 Generated with [Claude Code](https://claude.com/claude-code)
