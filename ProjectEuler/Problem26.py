def tekrar_eden_dizi_uzunlugu(payda):
    kalan = 1
    gorulen_kalanlar = {}
    pozisyon = 0

    while kalan not in gorulen_kalanlar:
        gorulen_kalanlar[kalan] = pozisyon
        kalan = (kalan * 10) % payda
        pozisyon += 1

    return pozisyon - gorulen_kalanlar[kalan]

def en_uzun_tekrar_eden_dizi(limit):
    en_uzun_dizi = 0
    sonuc = 0

    for payda in range(2, limit):
        dizi_uzunlugu = tekrar_eden_dizi_uzunlugu(payda)
        if dizi_uzunlugu > en_uzun_dizi:
            en_uzun_dizi = dizi_uzunlugu
            sonuc = payda

    return en_uzun_dizi, sonuc

limit = 1000  # İstediğiniz bir üst sınır değeri de verebilirsiniz.
en_uzun_dizi, sonuc = en_uzun_tekrar_eden_dizi(limit)
print(f"En uzun tekrar eden dizi, 1/{sonuc} paydasında {en_uzun_dizi} uzunluğunda görünür.")
