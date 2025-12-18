# Buat Otak AI nya
#1. Import Library

import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

#2. Load Data V2
df = pd.read_csv('dataset_gaji_v2.csv')

#3. Terjemahkan Kata jadi Angka Bahasa(Encoding)
# Kita bikin kamus: SMA=0. S1=1, S2=2
kamus_pendidikan = {'SMA': 0, 'S1': 1, 'S2': 2}

# Kita Tempelkan kamus ke kolom Pendidikan 
df['Pendidikan'] = df['Pendidikan'].map(kamus_pendidikan)

# Cek apakah berhasil (harus muncul angka, bukan tulisan lagi)
print("Contoh data setelah diterjemahkan:")
print(df.head())

#3. Tentukan X (Fitur) & y (Target)
X = df[['Pengalaman', 'Pendidikan']]
y = df['Gaji']

#4. Latih Model
model = LinearRegression()
model.fit(X, y)

#5. Coba Tes Dulu (Prediksi)
# Misal: Pengalaman 5 Tahun, Lulusan S1 (Angka 1)
contoh_data = [[5, 1]]
prediksi = model.predict(contoh_data)

print(f"Tes Prediksi (5 Tahun, S1): Rp {int(prediksi[0])}")

#6. Simpan Model V2
joblib.dump(model, 'model_gaji_v2.pkl')
print("✅ Sukses! Model V2 berhasil dilatih dan disimpan!")