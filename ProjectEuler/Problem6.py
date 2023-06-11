kareler_toplami = 0
toplam_karesi = 0

for x in range(1, 101):
    kareler_toplami += x * x
    toplam_karesi += x

sonuc = kareler_toplami - (toplam_karesi * toplam_karesi)
print("Sonuç: {}".format(sonuc))