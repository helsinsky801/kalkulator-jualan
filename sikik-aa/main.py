import os
from src.database import memuat_produk, simpan_transaksi
from src.validator import ambil_input_int, ambil_input_float
from src.kalkulator import hitung_pesanan

def main():
    print("===TOOLS PENGHITUNG PESANAN BARANG+===")
    daftar_produk = memuat_produk()

    if not daftar_produk:
        print("Gagal memuat data produk. Program berhenti")
        return
    
    print("\nDaftar Produk Tersedia:")
    for kode, info in daftar_produk.items():
        print(f"[kode] {info['nama']} - Rp {info['harga']:,}")

    while True:
        pilihan = input("\nMasukan Kode Produk yang ingin di beli.").strip().upper()
        if pilihan in daftar_produk:
            break
        print("kode produk tidak valid. Silahkan coba lagi")

    produk_terpilih  = daftar_produk[pilihan]
    print(f"Anda memilih: {produk_terpilih['nama']} (Rp {produk_terpilih['harga']:,})")

    jumlah = ambil_input_int("Masukan Jumlah Barang: ", min_val=1)
    diskon = ambil_input_float("Masukan Diskon (%), ketik 0 jika tidak ada: ", min_val=0, max_val=100)

    hasil = hitung_pesanan(produk_terpilih['harga'], jumlah, diskon)

    print("\n" + "="*30)
    print("     RINGKASAN PESANAN     ")
    print("="*30)
    print(f"Nama Barang   : {produk_terpilih['nama']}")
    print(f"Harga Satuan  : Rp {produk_terpilih['harga']:,}")
    print(f"Jumlah        : {jumlah} pcs")
    print(f"Subtotal      : Rp {hasil['subtotal']:,}")
    print(f"Potongan (Disc): Rp {hasil['potongan']:,}")
    print(f"Pajak (PPN)   : Rp {hasil['pajak']:,}")
    print("="*30)
    print(f"TOTAL BAYAR   : Rp {hasil['total_akhir']:,}")
    print("="*30)

    simpan_transaksi(produk_terpilih['nama'], jumlah, hasil['total_akhir'])
    print("\n[Sukses] Transaksi telah berhasil di simpan ke data/riwayat_pesanan.csv!")

if __name__ == "__main__":
    main()