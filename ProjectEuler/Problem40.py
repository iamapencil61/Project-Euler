champernowne = ""
x = 1
while len(champernowne) < 1000000:
    champernowne += str(x)
    x += 1

def rakamlari_carp():
    sonuc = 1
    indeksler = [1, 10, 100, 1000, 10000, 100000, 1000000]

    for indeks in indeksler:
        basamak = int(champernowne[indeks-1])
        sonuc *= basamak

    return sonuc

sonuc = rakamlari_carp()
print(sonuc)
