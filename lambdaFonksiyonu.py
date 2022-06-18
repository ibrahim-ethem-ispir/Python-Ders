# lambda Fonksiyonu Nedir ?
# lambda fonksiyonu isimsiz(anonim) fonksiyonlardır. 
# lambda isimsiz fonksiyon tanımlamak için kullanılır.

firma = "kadim teknoloji"

def harfBul(a):
    return a in firma

# print(harfBul("z"))

bul = lambda a: a in firma

# print(bul("a"))

sayilar = [1, 3, 5, 7, 9]

usAl = list(map(lambda x : x ** 3, sayilar))

# print(usAl)

sayilarBul = list( map( lambda a : a in sayilar, [1, 7 ,12 , 15, 18]) )

print(sayilarBul)