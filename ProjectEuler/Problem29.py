farkliSonuclar = set()

for x in range(2, 101):
    for y in range(2, 101):
        sonuc = x ** y
        farkliSonuclar.add(sonuc)

sayac = len(farkliSonuclar)
print(f"Farklı sonuçlar: {sayac}")