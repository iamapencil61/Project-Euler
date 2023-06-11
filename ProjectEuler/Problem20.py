import math

def faktoriyelHesapla(n):
    return math.factorial(n)

n_faktoriyel = faktoriyelHesapla(n=100)

stringFaktoriyel = str(n_faktoriyel)

basamakToplami = 0

for basamak in stringFaktoriyel:
    basamakToplami += int(basamak)

print(f"Basamaklar toplamı: {basamakToplami}")