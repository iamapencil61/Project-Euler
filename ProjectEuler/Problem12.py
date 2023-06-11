def bolenBul(sayi):
    bolenler = []
    for x in range(1, int(sayi ** 0.5) + 1):
        if sayi % x == 0:
            bolenler.append(x)
            if x != sayi // x:
                bolenler.append(sayi // x)
    return bolenler

def ucgenSayininBolenleriBul(bolenSayaci):
    n = 1
    ucgenSayi = 1
    while True:
        bolenler = bolenBul(ucgenSayi)
        if len(bolenler) > bolenSayaci:
            return ucgenSayi
        n += 1
        ucgenSayi += n

bolenSayaci = 500
sonuc = ucgenSayininBolenleriBul(bolenSayaci)
print("Beş yüzden fazla bölene sahip olan ilk üçgensel sayı:", sonuc)
print("Bu üçgensel sayının bölenleri:", bolenBul(sonuc))
