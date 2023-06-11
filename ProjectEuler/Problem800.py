import time, math

baslangic_zamani = time.time()


def asal_mi(x):  # Verilen değerin asal olup olmadığını kontrol et
    if x <= 1:
        return False
    elif x <= 3:
        return True
    elif x % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(x)) + 1, 2):
            if x % i == 0:
                return False
        return True


def asal_olanlar_listesi(n):
    sonuc = [True] * (n + 1)
    sonuc[0] = sonuc[1] = False
    for i in range(int(math.sqrt(n)) + 1):
        if sonuc[i]:
            for j in range(2 * i, len(sonuc), i):
                sonuc[j] = False
    return sonuc


def asal_sayilari_listele(n):
    return [i for (i, asal_mi) in enumerate(asal_olanlar_listesi(n)) if asal_mi]


def asal_carpanlar(n):
    carpanlar = {}
    d = 2
    while n > 1:
        while n % d == 0:
            if d in carpanlar:
                carpanlar[d] += 1
            else:
                carpanlar[d] = 1
            n /= d
        d = d + 1
        if d * d > n:
            if n > 1:
                n = int(n)
                if d in carpanlar:
                    carpanlar[n] += 1
                else:
                    carpanlar[n] = 1
            break
    return carpanlar


def sonraki_asal(n):
    n += 1
    while True:
        if asal_mi(n):
            return n
        n += 1


def brute_force(n):
    asal_sayilar = asal_sayilari_listele(int(math.sqrt(n)))
    hibrit_tamsayilar = []
    for a in range(len(asal_sayilar)):
        p = asal_sayilar[a]
        for b in range(a + 1, len(asal_sayilar)):
            q = asal_sayilar[b]
            x = pow(p, q) * pow(q, p)
            if x <= n:
                hibrit_tamsayilar.append([x, p, q])
    return hibrit_tamsayilar


def asal_sayi_sayisi(limit):  # Diziyi döndürür, öyle ki dizi[x] = x'den küçük asal sayıların sayısı
    asal_uretec = asal_olanlar_listesi(limit + 50)
    asal_sayilari = [x for x in range(len(asal_uretec)) if asal_uretec[x]]
    dizi = [0] * (limit + 1)
    p_indeks = 0
    for x in range(1, limit + 1):
        while True:
            if asal_sayilari[p_indeks] > x:
                dizi[x] = p_indeks
                break
            p_indeks += 1
    return dizi


def C(a, b):
    # Hesaplamayı logaritmik terimlerle yap
    # q*log(p) + p*log(q) < b*log(a)
    limit = math.log(a, 10) * b
    sayac = 0
    p = 2
    while True:
        p_log = math.log(p, 10)
        if 2 * p * p_log > limit:
            break

        # Bir sonraki asal ve limit/p_log arasında ikili arama yaparak
        # q*log(p) + p*log(q) > b*log(a) olacak en küçük q'yu bul
        lo = sonraki_asal(p)
        hi = limit // p_log
        while lo < hi:
            q = (lo + hi) // 2
            q_log = math.log(q, 10)
            if p * q_log + q * p_log > limit:
                hi = q
            else:
                lo = q + 1

        q = int(q)
        if not asal_mi(q):
            q = sonraki_asal(q)
        q_log = math.log(q, 10)

        if p == 2:
            pp = asal_sayi_sayisi(sonraki_asal(q))

        if p * q_log + q * p_log == limit:
            sayac += (pp[q] - pp[p])

        elif p * q_log + q * p_log > limit:
            sayac += (pp[q] - pp[p] - 1)

        elif p * q_log + q * p_log < limit:
            q = sonraki_asal(q)
            sayac += (pp[q] - pp[p] - 1)

        p = sonraki_asal(p)

    return sayac


if __name__ == "__main__":
    print(C(800800, 800800))
    print("--- %s saniye ---" % (time.time() - baslangic_zamani))