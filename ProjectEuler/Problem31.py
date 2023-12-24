def madeni_para_yollari(hedef, paralar):
    # her miktar için kaç farklı kombinasyon var
    yollar = [0] * (hedef + 1)

    # Başlangıç durumu
    yollar[0] = 1

    for madeni_para in paralar:
        # Alt miktarlardan başlayarak, hedefe kadar olan her miktar için
        for x in range(madeni_para, hedef + 1):
            # Her adımda yeni bir kombinasyon ekleniyor
            yollar[x] += yollar[x - madeni_para]
    # En sonunda hedef miktar için kaç farklı kombinasyon olduğunu döndür
    return yollar[hedef]

# Test için verilen problem
hedef_miktar = 200
madeni_para_damgalari = [1, 2, 5, 10, 20, 50, 100, 200]

sonuc = madeni_para_yollari(hedef_miktar, madeni_para_damgalari)
print(sonuc)