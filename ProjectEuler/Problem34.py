def faktoriyel(n):
    sonuc = 1
    for x in range(1, n + 1):
        sonuc *= x
    return sonuc

merakliSayilar = []

for y in range(3, 10 ** 6):
    faktoriyelBasamakToplami = sum(faktoriyel(int(basamak)) for basamak in str(y))
    if y == faktoriyelBasamakToplami:
        merakliSayilar.append(y)

sonuc = sum(merakliSayilar)
print(f"Sonuç: {sonuc}")