nomor = 0
def luasSegitiga () :
    alas = int(input("Masukan Alas :"))
    tinggi = int(input("Masukan Tinggi :"))
    luas =(alas * tinggi)/2
    return luas

def luasLingkaran ():
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


while nomor < 4:
    print ("-- Silahkan Pilih menu anda --")
    print ("1. Menghitung Luas Segitiga")
    print ("2. Menghitung Lingkaran")
    print ("3. Menghitung Volume Tabung")
    print ("4. Selesai")
    
    x = int(input('Masukan Menu yang anda pilih : '))

    if x == 1 :
        print(luasSegitiga())
    elif x == 2 :
        print(luasLingkaran())
    elif x == 3 :
        print(volumeTabung())
    else :
        print ("System Shutdown")
        break
    
    
    