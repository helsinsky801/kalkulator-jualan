import os 
import json
import csv
from datetime import datetime

PATH_PRODUK = os.path.join("data", "produk.json")
PATH_RIWAYAT = os.path.join("data", "riwayat_pesanan.csv")

def memuat_produk():
    """Membaca daftar produk dari file JSON"""
    if not os.path.exists(PATH_PRODUK):
        os.makedirs("data", exist_ok=True)
        data_default = {
            "B001": {"nama": "Laptop Asus ROG", "harga": 15000000}
        }
        with open(PATH_PRODUK, "w") as f:
            json.dump(data_default, f, indent=4)
        return data_default

    with open(PATH_PRODUK, "r") as f:
        return json.load(f)  

def simpan_transaksi(nama_barang, jumlah, total_bayar):
    """Mencatat transaksi sukses ke dalam file CSV."""  
    os.makedirs("data", exist_ok=True)
    file_baru = not os.path.exists(PATH_RIWAYAT)

    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(PATH_RIWAYAT, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if file_baru:
            writer.writerow(["Waktu", "Nama Barang", "Jumlah", "Total Bayar"])
        writer.writerow([waktu, nama_barang, jumlah, total_bayar])    