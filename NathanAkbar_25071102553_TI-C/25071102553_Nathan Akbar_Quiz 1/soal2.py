
Buku = [
    ['Bumi', 5000],
    ['Bulan', 7000],
    ['Matahari', 9000],
    ['Bintang', 8000],
    ['Komet', 6000],
]

pinjaman = []

while True:

    pilihan = int(input("\nMasukkan nomor buku yang akan dipinjam : "))

    if pilihan == 0:
        break

    elif 1 <= pilihan <= len(Buku):
        lama_pinjam = int(input('Berapa lama buku dipinjam : '))
        buku_pinjam = []

        
        nama_buku = Buku[pilihan-1][0]
        denda_buku = Buku[pilihan-1][1]

        pinjaman.append([nama_buku, denda_buku, lama_pinjam])
        buku_pinjam.append(lama_pinjam)
        

        print("Pinjaman ditambahkan!")

    else:
        print("Nomor buku tidak valid!")

print("\n Daftar Pinjaman")

total = 0

for item in pinjaman:

    nama_buku = item[0]
    denda_buku = item[1]
    lama_pinjam = item[2]
   
    subtotal = denda_buku * lama_pinjam
    total += subtotal

    print(denda_buku, "x", lama_pinjam, "= Rp", subtotal)

print("\nTotal Pinjaman: Rp", total)