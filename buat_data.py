import pandas as pd
# 1. Membuat contoh data gaji berdasarkan tahun pengalaman
data = {
        'Tahun_Pengalaman': [1, 2, 3, 4, 5], 
        'Gaji': [6000000, 8000000, 10000000, 12000000, 15000000]
}
# 2. Mengubah data menjadi DataFrame dan menyimpannya ke file CSV
df = pd.DataFrame(data)
print(df)
df.to_csv("dataset_gaji.csv", index=False)
