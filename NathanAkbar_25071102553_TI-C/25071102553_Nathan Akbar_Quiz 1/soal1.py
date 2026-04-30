
Buku = [
   ['Bumi', 5000],
    ['Bulan', 7000],
    ['Matahari', 9000],
    ['Bintang', 8000],
    ['Komet', 6000],
]

for i in range(len(Buku)):
    print(i+1, "Nama Buku:", Buku[i][0], "denda:", Buku[i][1])

pilihan = int(input("\nMasukkan nomor buku yang dipilih: "))

if pilihan >= 1 and pilihan <= len(Buku):
    nama_buku = Buku[pilihan-1][0]
    denda_buku = Buku[pilihan-1][1]

    print("\nBuku yang dipilih:", nama_buku)
    print("Denda: Rp", denda_buku)

else:
    print("\nError: Nomor menu tidak valid")
    