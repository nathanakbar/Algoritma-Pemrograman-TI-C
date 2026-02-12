#Fungsi membungkus kode agar bisa digunakan berulang kali.

# Definisi fungsi dengan argument
def hitung_luas(panjang, lebar):
    luas = panjang * lebar
    return luas

# Memanggil fungsi
hasil = hitung_luas(10, 5)
print("Luas Persegi:", hasil)