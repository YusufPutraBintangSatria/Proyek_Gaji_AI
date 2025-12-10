# 1. Panggil Alat & Bikin Judul
import streamlit as st #Kita panggil tukang webnya, kita kasih nama panggilan st
import joblib          # Perintah untuk bikin Tulisan Besar (Judul) di layar
import pandas as pd    # Perintah untuk bikin tulisan biasa (paragraf)

st.title("Prediksi Gaji IT")
st.write("Aplikasi ini dibuat oleh Bintang untuk menebak gaji.")

#2 Memanggil Otak AI & Membuat Input.
model = joblib.load("model_gaji.pkl")
tahun = st.slider("Pengalaman Kerja (Tahun):", 0, 20)

# 3. Tombol Ajaib (The Logic) 
if st.button("hitung Gaji"):
    # 1. Siapkan data (harus 2 kurung siku)
    data = [[tahun]]
    # 2. Prediksi
    hasil = model.predict(data)
    # 3. Tampilkan
    st.write("Gaji kamu kira-kira: Rp", int(hasil))
    