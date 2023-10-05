import requests
from bs4 import BeautifulSoup
import csv

# URL awal
base_url = "alamat web"

# Inisialisasi list untuk menyimpan data dari semua halaman
all_data = []

# Ketikan halaman pertama dan terakhir dalam kolom range dipisahkan tanda koma
for page_number in range(1, 100):
    # Buat URL lengkap dengan nomor halaman
    url = f"{base_url}{page_number}"

    # Kirim permintaan HTTP
    response = requests.get(url)

    # Hentikan loop jika tidak ada lagi halaman
    if response.status_code != 200:
        break

    # Parse halaman web dengan BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Ambil data yang Anda butuhkan dari halaman ini
    # Misalnya, Anda dapat menggunakan BeautifulSoup untuk mengekstrak tabel data

    # Misalnya, jika data yang Anda cari adalah dalam tabel, Anda dapat melakukan sesuatu seperti ini:
    table = soup.find("table")
    if table:
        for row in table.find_all("tr"):
            cells = row.find_all("td")
            if len(cells) == 3:  # Sesuaikan jumlah sel kolom sesuai kebutuhan
                data_row = {
                    "Kolom1": cells[0].get_text(strip=True),
                    "Kolom2": cells[1].get_text(strip=True),
                    "Kolom3": cells[2].get_text(strip=True),
                }
                all_data.append(data_row)

    # Tambahkan 1 ke nomor halaman untuk melanjutkan ke halaman berikutnya
    page_number += 1

# Sekarang, all_data berisi data dari semua halaman

# Simpan data ke dalam file CSV
csv_filename = "data_perusahaan.csv"

with open(csv_filename, mode="w", newline="", encoding="utf-8") as csv_file:
    fieldnames = ["Kolom1", "Kolom2", "Kolom3"]  # Gantilah dengan nama kolom yang sesuai
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # Tulis header kolom ke file CSV
    writer.writeheader()

    # Tulis data ke file CSV
    for data_row in all_data:
        writer.writerow(data_row)

print(f"Data telah disimpan ke dalam file {csv_filename}.")
