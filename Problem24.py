import itertools

basamaklar = list(range(10)) # 0'dan 9'a kadar rakamlar
permutasyon = list(itertools.permutations(basamaklar))

milyonuncuPermutasyon = "".join(map(str, permutasyon[999_999])) # 0 Tabanlı indeksleme
print(milyonuncuPermutasyon)

