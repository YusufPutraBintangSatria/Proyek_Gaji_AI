# Membuat aplikasi 

#import library yang dibutuhkan
from fastapi import FastAPI # pelayan website
import joblib # untuk memanggil otak AI yang sudah dilatih

app = FastAPI() # Menghidupkan aplikasi
model = joblib.load("model_gaji.pkl") # Memasang otak AI

# Membuat loketq layanan prediksi gaji
@app.get("/predict")
def prediksi_gaji(tahun_pengalaman: float):
    #1. Siapkan data (Ingat kurung siku ganda!)
    data = [[tahun_pengalaman]]
    #2. Suruh AI menebak
    hasil = model.predict(data)[0]
    # 3. Kembalikan hasil ke layar
    return {"prediksi_gaji": hasil}
