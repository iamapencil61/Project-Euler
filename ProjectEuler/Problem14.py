def collatzDizisi(n):
    baslangic = n
    liste = [baslangic]

    while baslangic != 1:
        if baslangic % 2 == 0:
            baslangic //= 2
        else:
            baslangic = 3 * baslangic + 1
        liste.append(baslangic)

    return liste, len(liste)

maksimumUzunluk = 0
maksimumSayi = 0

for sayi in range(1, 1000000):
    liste, uzunluk = collatzDizisi(sayi)
    if uzunluk > maksimumUzunluk:
        maksimumUzunluk = uzunluk
        maksimumSayi = sayi

print(f"En uzun collatz dizisi: {maksimumSayi}")
print(f"Dizi uzunluğu: {maksimumUzunluk}")