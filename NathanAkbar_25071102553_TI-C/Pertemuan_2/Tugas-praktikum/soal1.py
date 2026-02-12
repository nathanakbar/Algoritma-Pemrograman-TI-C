def rata_rata(nilai):
    # Cek apakah list kosong
    if len(nilai) == 0:
        return "Data kosong"
    
    # Hitung rata-rata
    total = sum(nilai)
    rata = total / len(nilai)
    return rata


# Memanggil fungsi dengan list nilai
data_nilai = [80, 75, 90, 60, 85]
hasil = rata_rata(data_nilai)

# Menampilkan hasil
print("Rata-rata nilai =", hasil)
