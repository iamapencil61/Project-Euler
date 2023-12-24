def permutasyonlar(sayi1, sayi2):
    return sorted(str(sayi1)) == sorted(str(sayi2))

def permutasyonKatlariniBul():
    x = 1
    while True:
        if all(permutasyonlar(x, y * x) for y in range(2, 7)):
            return x
        x += 1

sonuc = permutasyonKatlariniBul()
print("Sonuç:", sonuc)
