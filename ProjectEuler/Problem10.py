import math

def asalMi(n):
    """Bir sayının asal olup olmadığını kontrol eder."""
    if n < 2:
        return False
    for x in range(2, math.isqrt(n) + 1):
        if n % x == 0:
            return False
    return True

def asalUreteci(limit):
    """Verilen bir limit değerine kadar olan asal sayıları üretir."""
    asallar = []
    for i in range(2, limit):
        if asalMi(i):
            asallar.append(i)
    return asallar

# 2 milyondan küçük asal sayıları üret ve topla
asallar = asalUreteci(2000000)
print(sum(asallar))