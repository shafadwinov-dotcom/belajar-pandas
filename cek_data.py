
import pandas as pd

# Membaca data CSV
df = pd.read_csv("onlinefoods.csv")

# Menampilkan ukuran data
print(df.shape)

# Menampilkan 5 data pertama
print(df.head())

# Cek kesehatan data
df.info()

# Cek missing value
print("\nJumlah missing value:")
print(df.isna().sum())

# Cek duplicate
print("\nJumlah data duplicate:", df.duplicated().sum())

# Cek jumlah data pada setiap kolom
print("\nJumlah kategori setiap kolom:")
for kolom in df.select_dtypes(include="object").columns:
    print(f"\n{kolom}:")
    print(df[kolom].value_counts())

# Cek kolom dengan tipe data numerik
print("\nStatistik deskriptif:")
print(df.describe())

# Menghapus data duplikat
df = df.drop_duplicates()

# Mengecek kembali informasi data
print("\nInformasi data setelah menghapus duplikat:")
df.info()

# Memperbaiki penulisan data kategorikal
for kolom in df.select_dtypes(include="object").columns:
    df[kolom] = df[kolom].str.strip().str.title()

# Menampilkan hasil perbaikan
print("\nData setelah perbaikan penulisan:")
print(df.head())

# Menyimpan data yang sudah dibersihkan
df.to_csv("onlinefoods_bersih.csv", index=False)

print("\nData berhasil dibersihkan dan disimpan!")
