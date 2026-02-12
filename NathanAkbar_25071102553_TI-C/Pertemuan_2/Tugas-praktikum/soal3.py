def jumlah_digit(n):
    # Basis rekursi: jika n sudah 0
    if n == 0:
        return 0
    # Rekursi: digit terakhir + sisa digit
    else:
        return n % 10 + jumlah_digit(n // 10)


# Contoh pemanggilan
angka = 1234
hasil = jumlah_digit(angka)

# Menampilkan hasil
print("Jumlah digit dari", angka, "=", hasil)
