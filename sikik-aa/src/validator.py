def ambil_input_int(pesan, min_val=0):
    """Validasi input angka bulat agar terhindar dari error crash input teks."""
    while True:
        try:
            nilai = int(input(pesan))
            if nilai < min_val:
                print(f"input tidak boleh kurang dari{min_val}.")
                continue
            return nilai
        except ValueError:
            print("Input salah! harap masukan angka bulat yang valid.")

def ambil_input_float(pesan, min_val=0.0, max_val=100.0):
    """Validasi input angka desimal atau persen."""
    while True:
        try:
            nilai = float(input(pesan))
            if nilai < min_val or nilai > max_val:
                print(f"Input harus berada di antara {min_val} dan {max_val}.")
                continue
            return nilai
        except ValueError:
            print("Input salah! Harap masukan angka yang valid")