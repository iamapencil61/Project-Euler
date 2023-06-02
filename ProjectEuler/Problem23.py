def bolSayiMi(n):
    bolenlerToplami = sum(x for x in range(1, n) if n % x == 0)
    return bolenlerToplami > n

limit = 28123 # Belirli sınıra kadar olan sayılar kontrol edilecek
bolSayilar = set(x for x in range(1, limit) if bolSayiMi(x))
def bolSayilarToplami(n):
    for bolSayi in bolSayilar:
        if n - bolSayi in bolSayilar:
            return True
    return False

sonuc = sum(x for x in range(1, limit) if not bolSayilarToplami(x))
print(f"Sonuç: {sonuc}")