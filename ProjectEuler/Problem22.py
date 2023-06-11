with open("isimler.txt", "r") as dosya:
    isimler = [isim.strip('"') for isim in dosya.read().split(",")]
    isimler.sort()

def adDegeri(isim):
    deger = 0
    for harf in isim:
        deger += ord(harf.upper()) - ord("A") + 1
    return deger

adDegerleri = [adDegeri(isim) for isim in isimler]

skorlar = [adDegeri * (index + 1) for index, adDegeri in enumerate(adDegerleri)]
toplamSkor = sum(skorlar)
print(f"Toplam skor: {toplamSkor}")