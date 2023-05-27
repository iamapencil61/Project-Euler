for a in range(1, 1000):
    for b in range(a, 1000):
        c = 1000 - (a + b)
        if a ** 2 + b ** 2 == c ** 2:
            if a + b + c == 1000:
                sonuc = a * b * c
                print(sonuc)
                break
    else:
        continue
    break