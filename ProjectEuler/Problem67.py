def maksYolToplami(ucgen):
    for x in range(len(ucgen)-2, -1, -1):  # Üçgenin altından başlayarak yukarı doğru tara
        for y in range(len(ucgen[x])):
            # Altındaki iki sayıdan maksimumunu seçip üst satırdaki sayıya ekleyelim
            ucgen[x][y] += max(ucgen[x+1][y], ucgen[x+1][y+1])
    return ucgen[0][0]  # En üstteki elemanı döndür

# Üçgeni dosyadan okuyalım
ucgen = []
with open("triangle.txt", "r") as file:
    for line in file:
        satir = [int(sayi) for sayi in line.strip().split()]
        ucgen.append(satir)

# Fonksiyonu çağırarak sonucu alalım
sonuc = maksYolToplami(ucgen)
print("Maksimum toplam:", sonuc)