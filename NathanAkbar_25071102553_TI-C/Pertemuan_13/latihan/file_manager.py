import os

def daftar_file():
    files = [file for file in os.listdir() if file.endswith(".txt")]
    return files

while True:
    print("========================")
    print("PYTHON FILE MANAGER v1.0")
    print("=========================")
    print("[1] Read file")
    print("[2] Write file")
    print("[3] Delete file")
    print("[0] Exit")

    menu = input("Pilih menu: ")


    if menu == "1":
        files = daftar_file()

        if len(files) == 0:
            print("Tidak ada file .txt ditemukan.")
            continue

        print("\nFile tersedia:")
        for i, file in enumerate(files, start=1):
            print(f"[{i}] {file}")

        try:
            pilih = int(input("Pilih file (nomor): "))
            nama_file = files[pilih - 1]

            with open(nama_file, "r") as file:
                isi = file.read()

            print(f"\n--- Isi {nama_file} ---")
            print(isi)
        except:
            print("Input tidak valid!")

    elif menu == "2":
        files = daftar_file()

        print("\nFile tersedia:")
        for i, file in enumerate(files, start=1):
            print(f"[{i}] {file}")

        nama_file = input(
            "\nMasukkan nama file baru / nama file lama: "
        )

        if not nama_file.endswith(".txt"):
            nama_file += ".txt"

        isi = input("Masukkan isi file: ")

        try:
            with open(nama_file, "w") as file:
                file.write(isi)

            print("File berhasil disimpan.")

        except:
            print("Gagal menulis file!")

    
    elif menu == "3":
        files = daftar_file()

        if len(files) == 0:
            print("Tidak ada file .txt ditemukan.")
            continue

        print("\nFile tersedia:")
        for i, file in enumerate(files, start=1):
            print(f"[{i}] {file}")

        try:
            pilih = int(input("Pilih file yang ingin dihapus: "))
            nama_file = files[pilih - 1]

            konfirmasi = input(
                f"Yakin ingin menghapus {nama_file}? (y/n): "
            )

            if konfirmasi.lower() == "y":
                os.remove(nama_file)
                print("File berhasil dihapus.")
            else:
                print("dibatalkan.")

        except:
            print("Input tidak valid!")

    
    elif menu == "0":
        print("Program selesai.")
        break

    else:
        print("Menu tidak tersedia!")