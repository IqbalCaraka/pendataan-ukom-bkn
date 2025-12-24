import csv
from datetime import datetime

# Path file CSV
file_path = r"d:\Kantor\2025\Pokja Pengembangan Kompetensi\Usul Uji Kompetensi\Pelaporan\Pelaporan Pengolahan TWIII.csv"

# Mapping nama bulan dalam Bahasa Indonesia
bulan_indonesia = {
    1: 'Januari',
    2: 'Februari',
    3: 'Maret',
    4: 'April',
    5: 'Mei',
    6: 'Juni',
    7: 'Juli',
    8: 'Agustus',
    9: 'September',
    10: 'Oktober',
    11: 'November',
    12: 'Desember'
}

# Mapping nama bulan untuk parsing (termasuk bahasa Inggris)
bulan_parsing = {
    'Januari': 1, 'Februari': 2, 'Maret': 3, 'April': 4,
    'Mei': 5, 'Juni': 6, 'Juli': 7, 'Agustus': 8,
    'September': 9, 'Oktober': 10, 'November': 11, 'Desember': 12,
    'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4,
    'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8,
    'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
}

# Fungsi untuk normalisasi tanggal ke format "dd Bulan yyyy"
def normalize_tanggal(tanggal):
    if not tanggal or tanggal.strip() == '':
        return ''

    try:
        tanggal = tanggal.strip()

        # Format: "8-Apr-25" atau "dd-Mon-yy"
        if '-' in tanggal:
            parts = tanggal.split('-')
            if len(parts) == 3:
                day = parts[0].zfill(2)  # Tambahkan leading zero
                month_abbr = parts[1]
                year = parts[2]

                # Konversi tahun 2 digit ke 4 digit
                if len(year) == 2:
                    year = '20' + year

                # Konversi bulan singkatan ke nama penuh
                if month_abbr in bulan_parsing:
                    month_num = bulan_parsing[month_abbr]
                    month_name = bulan_indonesia[month_num]
                    return f"{day} {month_name} {year}"

        # Format: "07 Januari 2025" (sudah benar)
        parts = tanggal.split()
        if len(parts) == 3 and parts[1] in bulan_parsing:
            day = parts[0].zfill(2)
            return f"{day} {parts[1]} {parts[2]}"

        # Format lain: dd/mm/yyyy, yyyy-mm-dd, etc.
        for fmt in ['%d/%m/%Y', '%Y-%m-%d', '%m/%d/%Y', '%d-%m-%Y']:
            try:
                dt = datetime.strptime(tanggal, fmt)
                return f"{dt.day:02d} {bulan_indonesia[dt.month]} {dt.year}"
            except ValueError:
                continue

        return tanggal  # Kembalikan original jika tidak bisa diparse
    except:
        return tanggal

# Fungsi untuk mengkonversi tanggal ke nama bulan
def tanggal_ke_bulan(tanggal):
    if not tanggal or tanggal.strip() == '':
        return ''

    try:
        # Format: "07 Januari 2025" atau "dd Month yyyy"
        parts = tanggal.strip().split()
        if len(parts) == 3 and parts[1] in bulan_parsing:
            return parts[1]

        return ''
    except:
        return ''

# Baca file CSV
rows = []
with open(file_path, 'r', encoding='utf-8-sig', newline='') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames

    # Proses setiap baris
    for row in reader:
        # Normalisasi format tanggal di kolom TANGGAL EMAIL MASUK
        tanggal_email = row.get('TANGGAL EMAIL MASUK', '')
        tanggal_normalized = normalize_tanggal(tanggal_email)
        row['TANGGAL EMAIL MASUK'] = tanggal_normalized

        # Konversi ke nama bulan untuk kolom BULAN PENGAJUAN
        row['BULAN PENGAJUAN'] = tanggal_ke_bulan(tanggal_normalized)
        rows.append(row)

# Tulis kembali ke file CSV
with open(file_path, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("File CSV berhasil diupdate!")
print(f"\nContoh 10 baris pertama:")
print(f"{'TANGGAL EMAIL MASUK':<30} {'BULAN PENGAJUAN':<15}")
print("-" * 45)
for i, row in enumerate(rows[:10]):
    print(f"{row.get('TANGGAL EMAIL MASUK', ''):<30} {row.get('BULAN PENGAJUAN', ''):<15}")

print(f"\nTotal {len(rows)} baris telah diproses.")
print("\nCatatan: Format tanggal di kolom 'TANGGAL EMAIL MASUK' telah dinormalisasi menjadi 'dd Bulan yyyy'")
