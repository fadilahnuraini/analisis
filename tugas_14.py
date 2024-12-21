# -*- coding: utf-8 -*-
"""Tugas 14.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pBO9QxsEhUnjNRR0r5dMG3rSyWwOBhNU

Langkah : 1
Pertama, kita perlu membuat Dataframe dari dataset, dan bahkan
sebelum itu pustaka tertentu harus diimpor
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
Order_Details = pd.read_csv('/content/online_sales_dataset.csv')

Order_Details.head()

"""Buat kolom baru bernama Time yang memiliki format DateTime setelah
mengonversi kolom Transaction Date ke dalamnya. Format DateTime,
yang memiliki pola YYYY-MM-DD HH:MM:SS , dapat disesuaikan
sesuai keinginan Anda. Di sini kita lebih tertarik untuk memperoleh jam,
jadi kita dapat memiliki kolom Hour dengan menggunakan fungsi
bawaan untuk hal yang sama

"""

# Convert 'InvoiceDate' column to DateTime
Order_Details['Time'] = pd.to_datetime(Order_Details['InvoiceDate'], format='%Y-%m-%d %H:%M')

# Extract hour from the 'Time' column and create a new 'Hour' column
Order_Details['Hour'] = Order_Details['Time'].dt.hour

# Display the DataFrame to verify the new columns
print(Order_Details[['InvoiceDate', 'Time', 'Hour']].head())

import pandas as pd

# Assuming the DataFrame is already loaded as Order_Details
# and the 'Hour' column has been properly formatted.

# Calculate the count of transactions per hour
hourly_counts = Order_Details['Hour'].value_counts()

# Sort the counts in descending order to get the busiest hours first
sorted_hourly_counts = hourly_counts.sort_values(ascending=False)

# Select the top 24 busiest hours
n = 24  # Modify as needed
top_hours = sorted_hourly_counts.head(n).index.tolist()
top_counts = sorted_hourly_counts.head(n).values.tolist()

# Print the results
print("Top 24 busiest hours:", top_hours)
print("Number of transactions per hour:", top_counts)

"""Terakhir, menumpuk indeks (jam) dan frekuensi bersama-sama untuk
menghasilkan hasil akhir.
"""

import numpy as np
import pandas as pd

# Assuming Order_Details DataFrame is loaded
# Get the counts of transactions per hour and sort them if needed
hourly_transaction_counts = Order_Details['Hour'].value_counts().sort_index()

# Get top 24 busiest hours, assuming 24 is the desired number of entries
timemost1 = hourly_transaction_counts.index.tolist()[:24]
timemost2 = hourly_transaction_counts.values.tolist()[:24]

# Stack the hour and transaction count arrays together for better alignment
tmost = np.column_stack((timemost1, timemost2))

# Print headers and each row of the stacked data
print(" Hour Of Day" + "\t" + "Cumulative Number of Purchases \n")
print('\n'.join('\t\t'.join(map(str, row)) for row in tmost))

"""Sebelum kita dapat membuat visualisasi data yang sesuai, kita harus
membuat daftar sedikit lebih yang dapat disesuaikan. Untuk
melakukannya, adalah dengan mengumpulkan frekuensi per jam dan
melakukan tugas-tugas berikut
"""

import pandas as pd
import matplotlib.pyplot as plt

# Diasumsikan DataFrame Order_Details sudah dimuat
# Menghitung frekuensi transaksi per jam
hitungan_transaksi_perjam = Order_Details['Hour'].value_counts()

# Membuat DataFrame yang mencakup semua jam dari 0 sampai 23
jam = pd.DataFrame({'Jam': range(24)})

# Menggabungkan ini dengan hitungan transaksi per jam untuk memastikan semua jam terwakil
data_jam = pd.merge(jam, hitungan_transaksi_perjam, left_on='Jam', right_index=True, how='left').fillna(0)

# Mengubah nama kolom untuk kejelasan
data_jam.columns = ['Jam', 'Jumlah Transaksi']

# Mengonversi Jumlah Transaksi menjadi integer
data_jam['Jumlah Transaksi'] = data_jam['Jumlah Transaksi'].astype(int)

# Sekarang data_jam siap untuk divisualisasikan atau dimanipulasi lebih lanjut
print(data_jam.head())

# Visualisasi data menggunakan diagram batang
plt.figure(figsize=(10, 6))
plt.bar(data_jam['Jam'], data_jam['Jumlah Transaksi'], color='skyblue')
plt.xlabel('Jam Dalam Sehari')
plt.ylabel('Jumlah Transaksi')
plt.title('Frekuensi Transaksi Per Jam')
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt
import pandas as pd

# Assuming timemost2 is already a properly structured DataFrame with hour indices from 0 to 23
# If timemost2 was created as instructed in previous responses, it should be ready.

# Check the data structure again
print("Structure of timemost2:")
print(timemost2.head())

# Ensure we have data for all 24 hours, correct the range if necessary
hour_list = list(range(24))  # Correcting the range to include all 24 hours from 0 to 23

# Extract the transaction counts
transaction_counts = timemost2['Jumlah Transaksi'].tolist()  # This should also have 24 items if indexed correctly

# Validate lengths
print("Length of hour_list:", len(hour_list))
print("Length of transaction_counts:", len(transaction_counts))

# Plotting the data
plt.figure(figsize=(20, 10))
plt.title('Sales Happening Per Hour (Spread Throughout The Week)', fontdict={'fontname': 'monospace', 'fontsize': 30}, y=1.05)
plt.ylabel("Number Of Purchases Made", fontsize=18, labelpad=20)
plt.xlabel("Hour", fontsize=18, labelpad=20)
plt.plot(hour_list, transaction_counts, color='m')  # Ensure this uses the correct data
plt.grid()
plt.show()