#Melatih otak ai untuk memprediksi gaji karyawan

# 1. Mengimport library yang dibutuhkan
import pandas as pd # untuk membaca file csv
from sklearn.linear_model import LinearRegression # untuk mengambil rumus matematika (model)
import joblib # untuk membungkus model yang sudah dilatih

# 2. Membaca data dari file csv
pd = pd.read_csv("dataset_gaji.csv")

# 3. Memisahkan mana soal dan mana kunci jawaban
X = pd[['Tahun_Pengalaman']] # Mengambil kolom pengalaman sebagai input
y = pd['Gaji'] # Mengambil kolom gaji sebagai target

# 4. Melatih model menggunakan Linear Regression
model = LinearRegression() # menyiapkan otak 
model.fit(X,y) # perintah "BElajar!". disini model mencari pola hubungan antara tahun dan gaji

# 5. menyimpan otak pintar ini ke dalam file
joblib.dump(model, "model_gaji.pkl") # model disimpan dalam file model_gaji.pkl
print("Model berhasi disimpan!")



