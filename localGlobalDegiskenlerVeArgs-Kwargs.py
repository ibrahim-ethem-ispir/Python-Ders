# Global Değişkenler tanımlandığı yerden sonra tüm satırlarda kullanılabilir.

# Local Değişkenler tanımlanan fonksiyon bloğu içerisinde kullanılır
#   fonksiyon görevini bitirikten sonra bellekten silinir.

a = 15
sayi = 37

"""
def test1():
    a = 7
    print("fonksiyon içerisinde : ",a)

test1()
print(a)


def test2():

    print("fonksiyon içerisinde : ", a)


test2()


def test3():
    global a
    print("değerini değiştirmeden : ", a)
    a = 105
    print("değeri değiştikrten sonra : ", a)
    sayi = 78
    print(sayi)

test3()

print(a)
print(sayi)

"""

"""
def test4(sayi1, sayi2):
    return sayi1 ** sayi2

usAl = test4(sayi2=2, sayi1=3)
print(usAl)
"""

def test5(*args, **kwargs):
    print(args)
    print(kwargs)

    sonuc = 0
    for i in args:
        sonuc += i * 4

    sonucKwargs = 0
    for j in kwargs:
        sonucKwargs += 2 * kwargs[j]
          
    print("kwargs : ", sonucKwargs)
    print("args : ",sonuc)


test5(1,2,3,4,5, a= 17, b=18)



