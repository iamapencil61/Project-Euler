def sarmalSayiKosegenleri(n):
    if n == 1:
        return 1
    toplam = 1
    mevcutNumara = 1

    for x in range(2, n + 1, 2):
        for y in range(4):
            mevcutNumara += x
            toplam += mevcutNumara
    return toplam

n = int(input("Spiral kenar uzunluğunu girin: "))
sonuc = sarmalSayiKosegenleri(n)
print(f"Çapraz köşelerdeki sayıların toplamı: {sonuc}")