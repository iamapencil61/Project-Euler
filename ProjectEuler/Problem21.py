def iki_sayi_arasindaki_bolenler(n):
    bolenler = []
    for x in range(1, n // 2 + 1):
        if n % x == 0:
            bolenler.append(x)
    return bolenler


def arkadasSayimi(n):
    bolenlerToplami = sum(iki_sayi_arasindaki_bolenler(n))
    return bolenlerToplami != n and sum(iki_sayi_arasindaki_bolenler(bolenlerToplami)) == n

def arkadasSayiCiftleri(ustSinir):
    arkadasSayilar = []
    for sayi in range(1, ustSinir):
        if arkadasSayimi(sayi):
            arkadasSayilar.append(sayi)
    return arkadasSayilar

def arkadasSayilarToplami(ustSinir):
    arkadasSayilar = arkadasSayiCiftleri(ustSinir)
    toplam = sum(arkadasSayilar)
    return toplam

ustSinir = 10000
sonuc = arkadasSayilarToplami(ustSinir)
print(f"Sınır değere kadar ki arkadaş sayılar toplamı: {sonuc}")