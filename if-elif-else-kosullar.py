# ======================= karşılaştırma Operatörleri =======================
# == iki değer birbirine eşitse 
# != iki değer birbirine eşit değilse 
# > soldaki değer sağdakinden büyükse
# < soldaki değer sağdakinden küçükse
# >= soldaki değer sağdakinden büyükse veya eşitse
# <= soldaki değer sağdakinden küçükse veya eşitse
"""
sayi1 = 5
sayi2 = 5

print(sayi1 != sayi2)
"""



# ================ Mantıksal Oparatörler =========================
# and -> ve oparatörürü 2 şart da sağlanırsa
# or -> veya oparatörü 2 şarttan 1 tane şart sağlanması yeterli
# not -> değil oparatörü
"""
a = True
b = 17
c = 20
d = 30

print(not a)
"""



# ====================== if - elif - else Koşulları ============================
# if -> Belirlenen şart sağlandığı zaman çalışan blok 
# elif -> if bloğundakinde şart sağlanmamışsa kontrol edilecek blok veya bloklar
# else -> if veya elif bloklarındaki şartlar sağlanmazsa çalışacak blok

sayi1 = 5
sayi2 = 17
"""
if sayi1 < sayi2:
    print("sayi1 küçüktür sayi2 den")
else:
    print("sayi1 ve sayi2 eşit değil")
"""
"""
karakter = input("Lütfen + , - , * , / karakterlerinden birini girin : ")

if karakter == "+":
    print("+ karakterine basıldı")
elif karakter == "-":
    print("- karakterine basıldı")
elif karakter == "*":
    print("* karakterine basıldı")
elif karakter == "/":
    print("/ karakterine basıldı")
else:
    print("Geçersiz karaktere bastınız")
"""

kayit = input("Sisteme Kayıtlımısınız :")
yetki = input("lütfen sistemdeki yetkinizi girin : ")


if kayit == "evet":
    print("Sisteme Hoş Geldiniz ... ")
    if yetki == "user":
        print("Anasayfaya Hoş Geldiz")
    elif yetki == "admin":
        print("Yönetici sayfasına hoş geldiniz")
    else:
        print("Lütfen doğru bir yetki adı girin")
else:
    print("Lütfen Kayıt Olun")
    print("Kayıt sayfasına yönlendiriliyorsunuz")
