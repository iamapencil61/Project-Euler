minSayi = 20
while True:
    bolunuyorMu = True
    for x in range(1, 21):
        if minSayi % x != 0:
            bolunuyorMu = False
            break
    if bolunuyorMu:
        break
    minSayi += 1

print(minSayi)
