def besinciKuvvetToplami(sayi):
    toplam = 0
    for rakam in str(sayi):
        toplam += int(rakam) ** 5
    return toplam

def toplamiBul():
    toplam = 0
    for sayi in range(5, 1000000):
        if sayi == besinciKuvvetToplami(sayi):
            toplam += sayi
    return toplam

sonuc = toplamiBul()
print(f"Sonuç: {sonuc}")