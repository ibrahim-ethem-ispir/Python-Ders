# ====================================================== For Döngüsü ============================================
#                Range() Fonksiyonu Belirlenen aralıklara göre sayıları getirmek için kullanılır
"""
for yazdir in range(1,50+1):
    print("merhaba : ",yazdir)

harfler = ["aaa","bbb","ccc","ddd"]
for harf in harfler:
    print(harf)


sayilar = [1,2,3,4,5]
for sayi in sayilar:
    print(sayi**2)


for i in range(1,50,10):
    print(i)

for x in range(1,60,7):
    if x % 2 == 1:
        print(x)

ogrenci = [("eren",50,90),("osman",75,65),("baki",75,100)]
for isim,vize,final in ogrenci:
    print(f"Öğrencinin Adı {isim} vize notu : {vize} final notu : {final}")
"""
for sayi1 in range(1,10+1):
    for sayi2 in range(1,10+1):
        print(f"{sayi1} kere {sayi2} : {sayi1*sayi2}")



