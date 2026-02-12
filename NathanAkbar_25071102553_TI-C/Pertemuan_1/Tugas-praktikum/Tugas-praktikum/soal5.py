# Membuat fungsi hitung
def hitung(a, b):
    penjumlahan = a + b
    pengurangan = a - b
    return penjumlahan, pengurangan

# Memanggil fungsi
hasil_tambah, hasil_kurang = hitung(5, 3)

# Menampilkan hasil
print("Penjumlahan =", hasil_tambah)
print("Pengurangan =", hasil_kurang)
