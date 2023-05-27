def asalMi(n):
    if n == 2:
        return True
    elif n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def kacinciAsal(n):
    sayac = 0
    sayi = 2
    while True:
        if asalMi(sayi):
            sayac += 1
            if sayac == n:
                return sayi
        sayi += 1

# 10001. asal sayıyı bulma
sonuc = kacinciAsal(10001)
print(sonuc)
