def pangkat_rekursif(a, b):
    # Basis rekursi
    if b == 0:
        return 1
    # Rekursi: a dikali hasil pangkat sebelumnya
    else:
        return a * pangkat_rekursif(a, b - 1)


# Contoh pemanggilan
a = 2
b = 5
hasil = pangkat_rekursif(a, b)

# Menampilkan hasil
print("Hasil", a, "pangkat", b, "=", hasil)
