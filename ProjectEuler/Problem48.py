toplam = 0

for x in range(1, 1001):
    toplam += x ** x
    toplam %= 10 ** 10

print(f"Serinin toplamı: {toplam}")
