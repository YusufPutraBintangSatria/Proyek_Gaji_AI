# Membuat resep pembuatan data

#1. Panggil alat dan siapkan bahan
import pandas as pd
import numpy as np

np.random.seed(42) # Agar hasil acaknya selalu sama(stabil)

jumlah_data = 1000 # Kita buat 1000 data karyawan palsu

#2. Membuat Data Mentah(Pengalaman & Pendidikan)
pengalaman = np.random.randint(0, 21, jumlah_data) # Acak pengalaman kerja(0-20 tahun)

pilihan = ['SMA', 'S1', 'S2'] #Acak pendidikan(SMA, S1, S2) Peluangnya: 20% SMA, 60% S1, 20% S2
pendidikan = np.random.choice(pilihan, jumlah_data, p=[0.2, 0.6, 0.2])

#3. Otak perhitungang gaji(Looping)
gaji = []

# Ulangi sampai 1000 kali
for i in range(jumlah_data):
    # Rumus Dasar: Gaji awal 3 juta + (Pengalaman x 1.5 juta)
    base = 3000000
    tambah_pengalaman = pengalaman[i] * 1500000

    # Cek pendidikan dia apa?
    tambah_pendidikan = 0
    if pendidikan[i] == 'S1':
        tambah_pendidikan = 2000000 # Bonus S1
    elif pendidikan[i] == 'S2':
        tambah_pendidikan = 5000000 # Bonus S2

    # Tambah Sedikit angka acak biar terlihat nyata (Noise)
    noise = np.random.randint(-500000, 500000)

    # Total Semuanya
    total = base + tambah_pengalaman + tambah_pendidikan + noise
    gaji.append(total)

#4. Bungkus & simpan(save)

# Satukan jadi Tabel(DataFrame)
df = pd.DataFrame({
    'Pengalaman': pengalaman,
    'Pendidikan': pendidikan,
    'Gaji': gaji
})

# Simpan jadi file baru (V2)
df.to_csv('dataset_gaji_v2.csv', index=False)
print("✅ Sukses! File 'dataset_gaji_v2.csv' telah dibuat.")
