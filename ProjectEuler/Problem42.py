with open("words.txt", "r") as dosya:
    kelimeler = dosya.read().replace('"', '').split(",")

harfPuanlari = {harf: indeks + 1 for indeks, harf in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}

def kelimenin_harf_puani(kelime):
    return sum(harfPuanlari[harf] for harf in kelime)

def ucgen_sayi_mi(sayi):
    n = int((2 * sayi) ** 0.5)
    return n * (n + 1) // 2 == sayi

ucgenKelimeSayisi = 0
for kelime in kelimeler:
    harfPuani = kelimenin_harf_puani(kelime)
    if ucgen_sayi_mi(harfPuani):
        ucgenKelimeSayisi += 1

print(ucgenKelimeSayisi)