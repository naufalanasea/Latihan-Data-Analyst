import pandas as pd
import matplotlib.pyplot as plt

# Import data CSV
df = pd.read_csv("data/bike-sharing\day.csv")

# Cek jumlah data
print(df.shape)

# Cek tipe data
print(df.dtypes)

# Cek distribusi data
df.hist()
plt.show()


year_counts = df.groupby("year").size()

# Plot grafik tren penggunaan 
plt.plot(year_counts)
plt.xlabel("Tahun")
plt.ylabel("Jumlah Penggunaan")
plt.title("Tren Penggunaan ")
plt.show()

# Analisis faktor-faktor yang mempengaruhi penggunaan 
# Hitung jumlah penggunaan  berdasarkan cuaca
weather_counts = df.groupby("weather").size()

# Plot bar chart penggunaan  berdasarkan cuaca
plt.bar(weather_counts.index, weather_counts)
plt.xlabel("Cuaca")
plt.ylabel("Jumlah Penggunaan")
plt.title("Penggunaan  Berdasarkan Cuaca")
plt.show()

# Hitung jumlah penggunaan berdasarkan hari libur
holiday_counts = df.groupby("holiday").size()

# Plot pie chart penggunaan  berdasarkan hari libur
plt.pie(holiday_counts, labels=holiday_counts.index)
plt.title("Penggunaan  Berdasarkan Hari Libur")
plt.show()

# Hitung jumlah penggunaan  berdasarkan waktu
hour_counts = df.groupby("hour").size()

# Plot line chart penggunaan  berdasarkan waktu
plt.plot(hour_counts)
plt.xlabel("Waktu")
plt.ylabel("Jumlah Penggunaan")
plt.title("Penggunaan Berdasarkan Waktu")
plt.show()

# Hitung jumlah penggunaan  berdasarkan lokasi
station_counts = df.groupby("station").size()

# Plot map chart penggunaan  berdasarkan lokasi
plt.scatter(df["latitude"], df["longitude"], c=df["station"])
plt.title("Penggunaan  Berdasarkan Lokasi")
plt.show()

