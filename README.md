# analisis
Analisis Penjualan Produk Aktif menggunakan Matplotlib di Python
# Hasil Analisis
## Metode
Proses analisis ini dilakukan menggunakan data transaksi yang terkumpul setiap jam selama seminggu. Data ini diolah untuk menentukan frekuensi transaksi per jam menggunakan Python dengan bantuan pustaka Pandas dan Matplotlib untuk visualisasi.
## Proses Pengolahan Data
1. Pengumpulan Data: Data transaksi diimpor dan diolah menggunakan pandas.
2. Ekstraksi Jam: Jam transaksi di ekstrak dari kolom Transaction Date yang kemudian disimpan dalam kolom baru Hour.
3. Penghitungan Frekuensi: Menggunakan value_counts() untuk menghitung frekuensi transaksi per jam dan disimpan dalam DataFrame untuk analisis lebih lanjut.
4. Persiapan Data Visualisasi: Data frekuensi yang sudah diurutkan dan disiapkan untuk visualisasi.
## Visualisasi
Visualisasi data dilakukan menggunakan Matplotlib, memvisualisasikan frekuensi transaksi per jam selama seminggu:

Judul: "Sales Happening Per Hour (Spread Throughout The Week)"
Sumbu X: Jam dalam sehari.
Sumbu Y: Jumlah transaksi.
Gaya Visualisasi: Plot garis dengan titik-titik data yang diwarnai magenta.

# Kesimpulan
Dari grafik yang dihasilkan, terlihat bahwa jam-jam tertentu memiliki frekuensi transaksi yang lebih tinggi dibandingkan dengan jam lainnya, yang memberikan wawasan penting untuk strategi penjualan dan penjadwalan staf.

# Implikasi
Hasil analisis ini dapat digunakan untuk mengoptimalkan operasi dan strategi pemasaran, dengan memfokuskan sumber daya pada jam-jam sibuk untuk meningkatkan efisiensi dan kepuasan pelanggan.
![image](https://github.com/user-attachments/assets/77256076-5c84-4fb5-a6db-b0251eb3f4b0)
