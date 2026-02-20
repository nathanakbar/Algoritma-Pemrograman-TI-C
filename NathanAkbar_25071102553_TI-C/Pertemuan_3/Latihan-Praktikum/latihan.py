class Vehicle:
    def __init__(self, jenis, merk, tahun_rilis):
        self.jenis = jenis
        self.merk = merk
        self.tahun_rilis = tahun_rilis
    
    def sound():
        return 'suara'
    
class Mobil(Vehicle):
    def __init__(self, jenis, merk, tahun_rilis, jumlah):
        Vehicle.__init__(self, jenis, merk, tahun_rilis)
        self.__jumlah = jumlah
        
    def get_jumlah(self):
         return self.__jumlah     
    
    def set_jumlah(self, jumlah):
            self.__jumlah = jumlah     
              
class Motor(Vehicle):
    def __init__(self, jenis, merk, tahun_rilis, harga):
        Vehicle.__init__(self, jenis, merk, tahun_rilis)
        self.__harga = harga
        
    def get_harga(self):
         return self.__harga
            
    def set_harga(self, harga):
        self.__harga = harga
        

Mobil =Mobil('Matic', 'Pajero_sport', '2019', '10')
Motor =Motor('Kopling', 'Supra', '2000', '25000000')

print(Mobil.get_jumlah())
print(Motor.get_harga())