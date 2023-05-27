a = 0
b = 1

toplam = 0

while b < 4000000:
    if b % 2 == 0:
        toplam += b
    a, b = b, a + b

print(toplam)
