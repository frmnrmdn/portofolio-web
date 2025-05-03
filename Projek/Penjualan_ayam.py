import pandas as pd 
import matplotlib.pyplot as plt 
import matplotlib.ticker as ticker

# Load data 
dataset = pd.read_csv("C:/Users/Manx/Documents/Folder Belajar Coding/Portofolio Web/Projek/penjualan_ayam_per_bagian.csv")
print(f"Menampilkan Dataset: \n", dataset.head(10))

# Menghitung data penjualan selama 6 bulan 
total_penjualan = dataset[['Paha_Atas', 'Paha_Bawah', 'Dada', 'Sayap']].mean()

# cari nilai max dari setiap potongan 
max_potongan = {
    'Paha_Atas': dataset['Paha_Atas'].max(),
    'Paha_Bawah': dataset['Paha_Bawah'].max(),
    'Dada': dataset['Dada'].max(),
    'Sayap': dataset['Sayap'].max(),
}

# Ubah dictionary jadi 2 list untuk plotting
bagian_ayam = list(max_potongan.keys())
penjualan_tertinggi = list(max_potongan.values())


# membuat bar chart 
plt.figure(figsize=(8,8))
bars = plt.bar(bagian_ayam, penjualan_tertinggi, color=['#FF9999', '#66B3FF', '#99FF99', '#FFCC99'])

# menambahkan angka diatas bar 
for bar in bars:
    yval = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2, # Posisi x: tengah batang 
        yval + 0.2,                         # Posisi y: sedikit diatas batang 
        f'{int(yval)}',                    # teks angka 
        ha='center', va='bottom'           # horizontal dan vertical alignment 
    )

plt.title("Penjualan Ayam Terbanyak per Bagian", fontsize=14)
plt.xlabel("Bagian Ayam", fontsize=12)
plt.ylabel("Jumlah Terjual", fontsize=12)
plt.gca().yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
plt.xticks(rotation=30)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

