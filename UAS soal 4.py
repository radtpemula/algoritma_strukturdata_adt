def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Kesalahan: Pembagian dengan nol tidak diperbolehkan."
    return a / b

def main():
    print("=== Kalkulator Sederhana ===")
    print("Pilih operasi:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")

    try:
        pilihan = int(input("Masukkan pilihan (1/2/3/4): "))
        if pilihan not in [1, 2, 3, 4]:
            print("Pilihan tidak valid!")
            return

        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))

        if pilihan == 1:
            print(f"Hasil: {tambah(a, b)}")
        elif pilihan == 2:
            print(f"Hasil: {kurang(a, b)}")
        elif pilihan == 3:
            print(f"Hasil: {kali(a, b)}")
        elif pilihan == 4:
            print(f"Hasil: {bagi(a, b)}")
    except ValueError:
        print("Harap masukkan input yang valid!")

if __name__ == "__main__":
    main()
