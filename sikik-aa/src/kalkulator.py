from config.setting import PAJAK_PPN_PERSEN

def hitung_pesanan(harga_satuan, jumlah, diskon_persen=0.0):
    """Menghitung rincian harga subtotal, diskon, pajak, hungga, total akhir."""
    subtotal = harga_satuan * jumlah
    potongan = subtotal * (diskon_persen / 100)

    setelah_diskon = subtotal - potongan
    pajak = setelah_diskon * (PAJAK_PPN_PERSEN / 100)

    total_akhir = setelah_diskon + pajak

    return {
        "subtotal": int(subtotal),
        "potongan": int(potongan),
        "pajak": int(pajak),
        "total_akhir": int(total_akhir)
    }