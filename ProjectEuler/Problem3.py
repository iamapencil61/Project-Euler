import math


def enBuyukAsalCarpan(sayi):
    while sayi % 2 == 0:
        sayi //= 2

    sayininKoku = math.isqrt(sayi) + 1
    for x in range(3, sayininKoku, 2):
        while sayi % x == 0:
            sayi //= x
            if sayi == 1:
                return x
    return sayi

sayi = 600851475143

sonuc = enBuyukAsalCarpan(sayi)
print(sonuc)