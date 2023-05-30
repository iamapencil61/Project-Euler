import time, math

başlangıç_zamanı = time.time()


def liste_oluşturucu(bir_sayı):
    uzunluk = len(str(bir_sayı))
    dizi = []
    for x in range(uzunluk + 1):
        dizi.append([])

    yığın = [bir_sayı]
    while len(yığın) != 0:
        şimdiki = yığın.pop(0)
        dizi[len(str(şimdiki))].append(şimdiki)

        if len(str(şimdiki)) == 1:
            continue

        ilk_haneden_kaldır = int(str(şimdiki)[1:])
        son_haneden_kaldır = şimdiki // 10

        yığın.append(ilk_haneden_kaldır)
        yığın.append(son_haneden_kaldır)

    for x in range(uzunluk + 1):
        dizi[x] = list(set(dizi[x]))
    return dizi


def bölümle(bir_sayı):
    cevap = set()
    cevap.add((bir_sayı,))
    for x in range(1, bir_sayı):
        for y in bölümle(bir_sayı - x):
            cevap.add(tuple(((x,) + y)))

    return sorted([x for x in cevap])


def hesapla(sınır):
    toplam = 0

    for z in range(1, sınır + 1):
        if z % 100000 == 0:
            print(z)
            print(toplam)
            print("--- %s saniye ---" % (time.time() - başlangıç_zamanı))
        if z % 9 == 0 or z % 9 == 1:
            x = z ** 2
            geçici_liste = bölümle(len(str(x)))[:-1]

            for y in geçici_liste:
                geçici_numara = str(x)
                geçici_toplam = 0
                değer = ""

                for z in y:
                    değer += geçici_numara[:z]
                    try:
                        geçici_toplam += int(geçici_numara[:z])
                    except ValueError:
                        pass
                    geçici_numara = geçici_numara[z:]
                    # print(değer)

                if değer == str(geçici_toplam ** 2):
                    toplam += x
                    break
    return toplam


if __name__ == "__main__":
    print(hesapla(10 ** 6))
    print("--- %s saniye ---" % (time.time() - başlangıç_zamanı))
