"""                             Python While Döngüsü ve Break, Continue Kullanımları
Break : Yazılmış olduğu yerde işlemi sonlandırır.
Continue : Yazılmış olduğu yerde oradaki döngü işlemini geçilmesini sağlar

while kosul:
    yapılacak işlemler

sayi = 1
while sayi <= 10:
    print("Merhaba",sayi)
    sayi += 1

sayi = 0
listem = ["aaa","bbb","ccc","ddd","eee"]
print(listem[3])
while sayi < len(listem):
    print((listem[sayi]))
    sayi += 1

sayi = 0
while sayi < 25:
    sayi += 1
    if sayi % 2 == 1:
        continue

    print(sayi)
"""
# 1 == ödenecek miktar
# 2 == elma = 3 tl
# 3 == portakal = 5 tl
# 4 == muz = 7 tl
# x == çıkış

tl = 0
while True:
    islem = input("Ne almak istersiniz : ")
    if islem == "x":
        print("Yine Bekleriz ...")
        break
    elif islem == "1":
        print(f"Toplam Ödenecek Tutar : {tl} Tl")
    elif islem == "2":
        kg = int(input("Kaç Kilogram Akmak İstersiniz : "))
        tl += kg * 3
    elif islem == "3":
        kg = int(input("Kaç Kilogram Almak İstersiniz : "))
        tl += kg * 5
    elif islem == "4":
        kg = int(input("Kaç Kilogram Almak İstersiniz : "))
        tl += kg * 7
    else:
        print("Bu ürün bulunmamaktardır !")
