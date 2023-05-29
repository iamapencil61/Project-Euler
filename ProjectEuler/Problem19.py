def artikYilMi(yil):
    if yil % 4 == 0:
        if yil % 100 == 0:
            if yil % 400 == 0:
                return True
            return False
        return True
    return False


def pazarSayaci():
    pazarlar = 0
    haftaninGunleri = 1  # 1 Ocak 1900 pazartesi olduğu için, 1 ile başlattım.

    for yil in range(1901, 2001):
        for ay in range(1, 13):
            # artık yıl kontrolü
            if ay == 2:
                if artikYilMi(yil):
                    ayinGunleri = 29
                else:
                    ayinGunleri = 28
            else:
                if ay in [4, 6, 9, 11]:
                    ayinGunleri = 30
                else:
                    ayinGunleri = 31

            # Pazar günlerini say
            if haftaninGunleri == 1:
                pazarlar += 1

            # Haftanın günleri değerini güncelle
            haftaninGunleri = (haftaninGunleri + ayinGunleri) % 7
    return pazarlar


sonuc = pazarSayaci()
print(sonuc)
