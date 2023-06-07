def asalMi(n):
    if n < 2:
        return False
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    return True

enBuyukAsal = 0
aSonucu = 0
bSonucu = 0

for a in range(-1000, 1001):
    for b in range(-1000, 1001):
        n = 0
        while True:
            sonuc = n ** 2 + a * n + b
            if not asalMi(sonuc):
                break
            n += 1
        if n >= enBuyukAsal:
            enBuyukAsal = n
            aSonucu = a
            bSonucu = b

alinanSonuc = aSonucu * bSonucu

print(f"Çarpım: {alinanSonuc}")
print(f"En büyük asal sayı: {enBuyukAsal}")
print(f"a: {aSonucu}")
print(f"b: {bSonucu}")