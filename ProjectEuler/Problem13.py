with open("sayi.txt", "r") as dosya:
    satirlar = dosya.readlines()

toplam = 0

for x in satirlar:
    sayi = int(x)
    toplam += sayi

toplamString = str(toplam)
ilkOnBasamak = toplamString[:10]

print(f"İlk on basamak: {ilkOnBasamak}")