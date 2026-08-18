import unittest
from src.kalkulator import hitung_pesanan

class TestKalkulator(unittest.TestCase):
    def test_hitung_pesanan_tanpa_diskon(self):
        hasil = hitung_pesanan(10000, 2, 0)
        self.assertEqual(hasil["subtotal"], 20000)
        self.assertEqual(hasil["pajak"], 2200)
        self.assertEqual(hasil["total_akhir"], 22200)

if __name__ == "__main__":
    unittest.main()