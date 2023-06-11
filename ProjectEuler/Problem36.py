def palindromMu(sayi):
    sayiStr = str(sayi)
    return sayiStr == sayiStr[::-1]

def problemiCoz():
    toplam = 0
    for sayi in range(1, 1000000):
        if palindromMu(sayi) and palindromMu(bin(sayi)[2:]):
            toplam += sayi
    return toplam

sonuc = problemiCoz()
print(f"Toplam: {sonuc}")