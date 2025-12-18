#1. Import Library
import streamlit as st
import pandas as pd
import joblib

#2. Load Model V2 (yang baru dilatih)
model = joblib.load('model_gaji_v2.pkl')

#3. Judul Web
st.title("Prediksi Gaji IT (Versi 2.0) 🤖")
st.write("Sekarang AI bisa membedakan gaji berdasarkan tingkat pendidikan!")

#4. Input 1: Pengalaman Kerja(Slider)
pengalaman = st.slider("Berapa tahun pengalaman kerja?", 0, 20, 1)

#5. Input 2: Tingkat Pendidikan (Dropdown/Pilihan)
# User memilih teks 'SMA', 'S1', atau 'S2'
pendidikan_opsi = st.selectbox("Apa tingkat pendidikan terakhir", ('SMA', 'S1', 'S2'))

#6. Tombol Prediksi
if st.button("Hitung Estimasi Gaji"):
    # A. Terjemahkan Pendidikan jadi angka(Encoding)
    # Kita harus konsisten sama 'kamus' di train_model.py tadi
    nilai_pendidikan = 0
    if pendidikan_opsi == 'SMA':
        nilai_pendidikan = 0
    elif pendidikan_opsi == 'S1':
        nilai_pendidikan = 1
    elif pendidikan_opsi == 'S2':
        nilai_pendidikan = 2

    # B. Siapkan Data untuk AI (Format harus 2 kolom: Pengalaman & Pendidikan)
    data_input = pd.DataFrame({
        'Pengalaman': [pengalaman],
        'Pendidikan': [nilai_pendidikan]
    })

    #C Prediksi
    hasil_gaji = model.predict(data_input)

    #D. Tampilkan Hasil (Dibulatkan jadi integer biar rapi)
    gaji_format = int(hasil_gaji[0])
    st.success(f"Estimasi Gaji Anda: Rp {gaji_format:,}")



