import os
os.system("cls")

def app_tebakangka():
    import random
    angka_acak = random.randint(1,10)
    makstebakan = 3
    tebakan = 0
    while tebakan < makstebakan:
        tebakan +=1
        angkauser = int(input("Masukkan angka tebakan : "))
        if angkauser > angka_acak:
            print("Angka terlalu besar, coba lagi : ")
        elif angkauser < angka_acak:
            print("Angka terlalu kecil, coba lagi : ")
        else:
            print("Selamat anda benar")
            break
    else:
        print(f"Kesempatan twbak kamu sudah habis, jawabannya adalah {angka_acak}")
        
    input("Enter jika lanjut")

def app_menu():
    while True:
        print("==Tebak Angka-==")
        print("1. Tebak Angka")
        print("2. Keluar")
        
        pilihan = str(input("Pilih (1 atau 2): "))
        if pilihan == 1:
            app_tebakangka()
            
        elif pilihan == 2:
            break
            
        else:
            print("Tolong masukkan angka yang benar!!!")
app_menu()