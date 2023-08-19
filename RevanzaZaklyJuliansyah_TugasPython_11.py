nomor = 0
menu = True

# Untuk Perhitungan Kalkulator
def penjumlahan ():
    angka1 = int(input("Masukan Angka Pertama :"))
    angka2 = int(input("Masukan Angka Kedua :"))
    jumlah = angka1 + angka2
    return jumlah

def pengurangan ():
    angka1 = int(input("Masukan Angka Pertama :"))
    angka2 = int(input("Masukan Angka Kedua :"))
    jumlah = angka1 - angka2
    return jumlah

def perkalian ():
    angka1 = int(input("Masukan Angka Pertama :"))
    angka2 = int(input("Masukan Angka Kedua :"))
    jumlah = angka1 * angka2
    return jumlah

def pembagian ():
    angka1 = int(input("Masukan Angka Pertama :"))
    angka2 = int(input("Masukan Angka Kedua :"))
    jumlah = angka1 / angka2
    return jumlah


# Untuk Menghitung Volume
def volumeBalok () :
    panjang = int(input("Masukan Alas :"))
    lebar = int(input("Masukan Lebar :"))
    tinggi = int(input("Masukan Tinggi :"))
    balok =panjang * lebar * tinggi
    return balok

def volumeBola ():
    phi = int(input("Masukan Phi : "))
    r   = int(input("Masukan Jari-Jari1 : "))
    r2   = int(input("Masukan Jari-Jari2 : "))

    L = phi * r * r2
    return L

def volumeTabung ():
    phi = int(input("Masukan Phi : "))
    r   = int(input("Masukan Jari-Jari : "))
    t   = int(input("Masukan Tinggi Tabung :"))

    v = phi * r * t
    return v

def kubus(sisi):
    volume = sisi ** 3
    luas_permukaan = 6 * sisi ** 2
    return volume, luas_permukaan

def balok(panjang, lebar, tinggi):
    volume = panjang * lebar * tinggi
    luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
    return volume, luas_permukaan

def tabung(jari_jari, tinggi):
    volume = math.pi * jari_jari ** 2 * tinggi
    luas_permukaan = 2 * math.pi * jari_jari * (jari_jari + tinggi)
    return volume, luas_permukaan
    
while menu == True:
        print("--MENU--")
        print("1. Program Perhitungan Kalkulator")
        print("2. Program Perhitungan Volume ")
        print("3. Program Perhitungan Bangun Ruang")
        print("4. Selesai")
        masukan = int(input('Masukan menu yang anda pilih : '))
        if masukan == 1 :
            while nomor < 5:
                print ("-- Selamat Datang Di Program Kalkulator --")
                print ("1. Penjumahan")
                print ("2. Pengurangan")
                print ("3. Perkalian")
                print ("4. Pembagian")
                print ("5. Kembali Kemenu Utama")
                x = int(input('Masukan Menu yang anda pilih : '))

                if x == 1 :
                    print(penjumlahan())
                elif x == 2 :
                    print(pengurangan())
                elif x == 3 :
                    print(perkalian())
                elif x == 4 :
                    print(pembagian())
                else :
                    break
        
                
        elif masukan == 2 :
            while nomor < 4:
                print ("-- Selamat Datang Di Program Perhitungan Volume --")
                print ("1. Menghitung Volume Balok")
                print ("2. Menghitung Volume Bola")
                print ("3. Menghitung Volume Tabung")
                print ("4. Selesai")
                x = int(input('Masukan Menu yang anda pilih : '))
            
                if x == 1 :
                    print(volumeBalok())
                elif x == 2 :
                    print(volumeBola())
                elif x == 3 :
                    print(volumeTabung())
                else :
                    break

        elif masukan == 3 :
            while nomor < 4:
                print("Program Perhitungan Bangun Ruang")
                print("1. Kubus")
                print("2. Balok")
                print("3. Tabung")
                print ("4. Selesai")
                x = int(input('Masukan Menu yang anda pilih : '))
            
                if x == 1:
                    sisi = float(input("Masukkan panjang sisi kubus: "))
                    volume, luas_permukaan = kubus(sisi)
                    print(f"Volume kubus: {volume}")
                    print(f"Luas permukaan kubus: {luas_permukaan}")
                elif pilihan == 2:
                    panjang = float(input("Masukkan panjang balok: "))
                    lebar = float(input("Masukkan lebar balok: "))
                    tinggi = float(input("Masukkan tinggi balok: "))
                    volume, luas_permukaan = balok(panjang, lebar, tinggi)
                    print(f"Volume balok: {volume}")
                    print(f"Luas permukaan balok: {luas_permukaan}")
                elif pilihan == 3:
                    jari_jari = float(input("Masukkan jari-jari tabung: "))
                    tinggi = float(input("Masukkan tinggi tabung: "))
                    volume, luas_permukaan = tabung(jari_jari, tinggi)
                    print(f"Volume tabung: {volume}")
                    print(f"Luas permukaan tabung: {luas_permukaan}")
                else :
                    print("System Shutdown")