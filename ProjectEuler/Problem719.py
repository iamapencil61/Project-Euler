import time, math

baslangic_zamani = time.time()


def liste_olusturucu(bir_sayi):
    uzunluk = len(str(bir_sayi))
    dizi = []
    for x in range(uzunluk + 1):
        dizi.append([])

    yigin = [bir_sayi]
    while len(yigin) != 0:
        simdiki = yigin.pop(0)
        dizi[len(str(simdiki))].append(simdiki)

        if len(str(simdiki)) == 1:
            continue

        ilk_haneden_kaldir = int(str(simdiki)[1:])
        son_haneden_kaldir = simdiki // 10

        yigin.append(ilk_haneden_kaldir)
        yigin.append(son_haneden_kaldir)

    for x in range(uzunluk + 1):
        dizi[x] = list(set(dizi[x]))
    return dizi


def bolumle(bir_sayi):
    cevap = set()
    cevap.add((bir_sayi,))
    for x in range(1, bir_sayi):
        for y in bolumle(bir_sayi - x):
            cevap.add(tuple(((x,) + y)))

    return sorted([x for x in cevap])


def hesapla(sinir):
    toplam = 0

    for z in range(1, sinir + 1):
        if z % 100000 == 0:
            print(z)
            print(toplam)
            print("--- %s saniye ---" % (time.time() - baslangic_zamani))
        if z % 9 == 0 or z % 9 == 1:
            x = z ** 2
            gecici_liste = bolumle(len(str(x)))[:-1]

            for y in gecici_liste:
                gecici_numara = str(x)
                gecici_toplam = 0
                deger = ""

                for z in y:
                    deger += gecici_numara[:z]
                    try:
                        gecici_toplam += int(gecici_numara[:z])
                    except ValueError:
                        pass
                    gecici_numara = gecici_numara[z:]
                    # print(deger)

                if deger == str(gecici_toplam ** 2):
                    toplam += x
                    break
    return toplam


if __name__ == "__main__":
    print(hesapla(10 ** 6))
    print("--- %s saniye ---" % (time.time() - baslangic_zamani))