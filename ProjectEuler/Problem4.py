
def palindromMu(sayi):
    strSayi = str(sayi)
    tersSayi = strSayi[::-1]
    if strSayi == tersSayi:
        return True
    else:
        return False

enBuyukPalindrom = 0

for x in range(100, 1000):
    for y in range(100, 1000):
        sayilariCarp = x * y
        if palindromMu(sayilariCarp) and sayilariCarp > enBuyukPalindrom:
            enBuyukPalindrom = sayilariCarp

print("En büyük çarpım: ", enBuyukPalindrom)