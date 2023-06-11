sayi_birimleri = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety'
}

def sayiyi_ingilizceye_cevir(sayi):
    if sayi < 20:
        return sayi_birimleri[sayi]
    elif sayi < 100:
        onlar_basamagi = sayi // 10 * 10
        birler_basamagi = sayi % 10
        return sayi_birimleri[onlar_basamagi] + '-' + sayi_birimleri[birler_basamagi]
    elif sayi < 1000:
        yuzler_basamagi = sayi // 100
        geri_kalan = sayi % 100
        if geri_kalan == 0:
            return sayi_birimleri[yuzler_basamagi] + ' hundred'
        else:
            return sayi_birimleri[yuzler_basamagi] + ' hundred and ' + sayiyi_ingilizceye_cevir(geri_kalan)
    elif sayi == 1000:
        return 'one thousand'

toplam_harf_sayisi = 0

for i in range(1, 1001):
    ingilizce_sayi = sayiyi_ingilizceye_cevir(i)
    harf_sayisi = len(ingilizce_sayi.replace('-', '').replace(' ', ''))
    toplam_harf_sayisi += harf_sayisi

print("Toplam harf sayısı:", toplam_harf_sayisi)