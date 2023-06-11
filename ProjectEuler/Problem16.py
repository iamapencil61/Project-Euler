sayi = 2 ** 1000
stringSayi = str(sayi)

toplam = 0
for basamak in stringSayi:
    tamSayiBasamak = int(basamak)
    toplam += tamSayiBasamak

print(toplam)
