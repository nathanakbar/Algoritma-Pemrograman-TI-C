#Fitur modern di Python (versi 3.10+) yang lebih rapi daripada banyak elif.

hari = "jumat"

match hari:
    case "Sabtu" | "Minggu":
        print("Waktunya libur!")
    case "Senin":
        print("Mulai bekerja")
    case _:
        print("Hari kerja biasa")