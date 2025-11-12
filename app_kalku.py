import os
os.system("cls")
def app_tambah():
    
    print("\nProgram Penjumlahan")
    try:
        angka1 = int(input("angka1:"))
        angka2 = int(input("angka2:"))
        hasil = angka1 + angka2
        print(hasil)
    except ValueError:
        print("input harus berupa angka")
    input("\nEnter untuk lanjut")
    
def app_kurang():
    try:
        print("\nPrograM pengurangan")
        angka1 = int(input("angka1:"))
        angka2 = int(input("angka2:"))
        hasil = angka1 - angka2
        print(hasil)
    except ValueError:
        print("Inputharis berupa angka")
    input("\nEnter untuk lanjut")
        
    
def app_kali():
    try:
        print("\nProgram Perkalian")
        angka1 = int(input("angka1:"))
        angka2 = int(input("angka2:"))
        hasil = angka1 * angka2
        print(hasil)
    except ValueError:
        print("input harus berupa angka")
    input("\nEnter untuk lanjut")
    
def app_bagi():
    try:
        print("\nprogram Pembagian")
        angka1 = int(input("angka1:"))
        angka2 = int(input("angka2:"))
        hasil = angka1 / angka2
        print(hasil)
    except ValueError:
        print("input harus berupa angka dan bukan nol")
    input("\nEnter untuk lanjut")
    
    
def app_menu():
    while True:
        print("\nProgram kalkulator")
        print("1. Pertambahan")
        print("2. Pengurangan")
        print("3. Perkaliam")
        print("4. Pembagian")
        print("5. Keluar")
        
        
        pilihan = int(input("Pilih Metode:"))
        if pilihan == 1:
            app_tambah()
        elif pilihan == 2:
            app_kurang()
        elif pilihan == 3:
            app_kali()
        elif pilihan == 4:
            app_bagi()
        elif pilihan == 5:
            break
        
app_menu()            