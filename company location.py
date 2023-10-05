import googlemaps
import pandas as pd

# Gantilah 'YOUR_API_KEY' dengan kunci API Google Maps Anda yang sebenarnya
api_key = 'YOUR_API_KEY'

# Inisialisasi klien Google Maps
gmaps = googlemaps.Client(api_key)

# Membaca daftar perusahaan dari file Excel
df = pd.read_excel('lokasi file.xlsx')

# Kolom yang berisi nama perusahaan dalam file Excel Anda
nama_perusahaan_column = 'Nama Perusahaan'

# Kolom yang akan digunakan untuk menyimpan alamat_column
alamat_column = 'Lokasi'


# Fungsi untuk mencari alamat perusahaan berdasarkan nama perusahaan
def cari_alamat(nama_perusahaan):
    try:
        # Mencari alamat menggunakan Google Maps Geocoding API
        hasil_geocode = gmaps.geocode(nama_perusahaan)

        # Jika hasil pencarian ditemukan, ambil alamat pertama dari hasil
        if hasil_geocode:
            alamat = hasil_geocode[0]['formatted_address']
            return alamat
        else:
            return "Alamat tidak ditemukan"
    except Exception as e:
        return str(e)


# Melakukan pencarian alamat untuk setiap perusahaan dalam DataFrame
df[alamat_column] = df[nama_perusahaan_column].apply(cari_alamat)

# Menyimpan hasil pencarian alamat ke dalam file Excel
df.to_excel('hasil_pencarian_alamat.xlsx', index=False)
