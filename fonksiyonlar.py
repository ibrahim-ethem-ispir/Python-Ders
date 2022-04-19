# fonksiyon kullanmanın bir diğer avantajı ise yazmış olduğunuz kod içerisinde değişiklik yapılması gerekiyorsa sadece fonksiyonu düzenlemeniz yeterli olur ama fonksiyon kullanmamış olsaydık o işlemleri kullandığımız her yerde düzenleme yapmamız gerekirdi.
# fonksiyonlar parametre almamışsa parametre gönderilmez
"""
print("merhaba")


def adSoyad():
    print("Merhaba 1")
    print("Merhaba 2")
    print("Merhaba 3")
    print("Merhaba 4")
    print("Merhaba 5")
    print("Merhaba 6")
    print("---------------------")


adSoyad()


adSoyad()


def adSoyad(ad, soyad):
    print(f"Adı : {ad} ve soyadı : {soyad} ")



adSoyad("ethem","ispir")
"""
import datetime as dt

def saatVeTarih():
    print(dt.datetime.now())


# saatVeTarih()


def donemHesapla(vize, final):
    harfNotu = ""
    ortalama = ( vize * 0.40 ) + ( final * 0.60 )
    if ( ortalama >= 85 ):
        harfNotu = "AA"
    elif ( ortalama >= 70 ):
        harfNotu = "BB"
    elif ( ortalama >= 50 ):
        harfNotu = "CC"
    elif ( ortalama >= 40 ):
        harfNotu = "DD"
    else:
        harfNotu = "FF"
    
    print(f"Öğrencinin Ortalaması : {ortalama} ve Harf Notu : {harfNotu} ")
    if (harfNotu == "FF"):
        print("Öğrenci Kaldı")



# donemHesapla(75,100)
# donemHesapla(50,60)
# donemHesapla(25,40)
# donemHesapla(85,90)


# return ifadesi fonksiyonun çalıştığı yere değer döndürür.

def usAl(sayi, ust):
    return sayi ** ust

usAl(2,4)
print(usAl(2,3))