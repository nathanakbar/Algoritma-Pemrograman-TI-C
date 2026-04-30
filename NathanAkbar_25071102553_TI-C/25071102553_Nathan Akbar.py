#===BAGIAN A===
DAFTAR_PILIHAN = ["gunting", "batu", "kertas", "batu", "gunting", "kertas", "gunting", "batu"]

riwayat =[]

def tentukan_pemenang(pilihan_pemain, pilihan_komputer):
    if pilihan_pemain == pilihan_komputer:
        return 'seri'
    elif (pilihan_pemain == "batu" and pilihan_komputer == "gunting") or \
        (pilihan_pemain == "gunting" and pilihan_komputer == "kertas") or \
        (pilihan_pemain == "kertas" and pilihan_komputer == "batu"):
        return "Pemain"
    else:
        return "komputer"
    
def main_satu_giliran(nomor_giliran):
    pilihan_komputer = DAFTAR_PILIHAN [nomor_giliran % len(DAFTAR_PILIHAN)]
    pilihan_pemain = ''
    
    while pilihan_pemain not in ['batu', 'gunting', 'kertas']:
        pilihan_pemain = input ('masukkan pilihan: ')
        if pilihan_pemain not in ['batu', 'gunting', 'kertas']:
            print('Tidak Valid')
    print(f'pilihan_komputer : {pilihan_komputer}')
    
    hasil = tentukan_pemenang(pilihan_pemain, pilihan_komputer)
    print(f">> Hasil babak ini untuk Pemain : {hasil[0]}")
    
    return [pilihan_pemain, pilihan_komputer, hasil[0]]
            
def main_satu_ronde(nama, nomor_ronde):
    nomor_giliran = 1
    pemain_win = 0
    komputer_win = 0
    print(f'Ronde: {nomor_ronde}')
    
    while pemain_win !=3 and komputer_win !=3 :
        nomor_giliran += 1
        menang = main_satu_giliran(nomor_giliran)
        if menang == 'pemain':
            pemain_win +=1
        elif menang == 'komputer':
            komputer_win +=1
    if pemain_win == 3:
        print('pemain menang ronde')
        score = pemain_win *10
    else:
        print('komputer menang ronde')
        score = 0
    return [nama, score]

def main():
  riwayat = []
  nama = input('Nama: ')
  nomor_ronde = 1
  lanjut = 'y'
  while lanjut == 'y':
    hasil = main_satu_ronde(nama, nomor_ronde)
    riwayat.append(hasil)
    nomor_ronde+=1
    lanjut = input('Lanjut?(y/n)')
  return riwayat
    
    
def tampilkan_riwayat(riwayat):
    if riwayat == []:
        print('Belum Ada Riwayat')
    return
    for i in range (len(riwayat)):
        print(f'{'No':<3} | {'Nama':<5} | {'Skor:<5'}|')
        print(f'{i+1}| {riwayat[i][0]} | {riwayat[i][1]}')
        
def bubble_sort_riwayat(riwayat):
    salin =riwayat.copy()
    n = len(salin)
    for i in range(n):
        for j in range(0, n-i-1):
            if salin[j][1] < salin[j+1][1]:
                salin[j],salin[j+1] = salin[j+1],salin[j]
                
    return salin

main()
       
 


    
       
    
    
             
            
        
    
        
       