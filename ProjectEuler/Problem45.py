def ucgenMi(n):
    x = (8 * n + 1) ** 0.5
    return x == int(x)

def besgenMi(n):
    x = (24 * n + 1) ** 0.5
    return x == int(x) and (int(x) + 1) % 6 == 0

def altigenMi(n):
    x = (8 * n + 1) ** 0.5
    return x == int(x) and (int(x) + 1) % 4 == 0

def enKucukOrtakSayiBul():
    n = 286

    while True:
        ucgen = n * (n + 1) // 2
        if besgenMi(ucgen) and altigenMi(ucgen):
            return ucgen
        n += 1


cozum = enKucukOrtakSayiBul()
print(f"Sonuç: {cozum}")