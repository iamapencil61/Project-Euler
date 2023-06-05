def asal_mi(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def daire_asal_mi(n):
    num_str = str(n)
    for _ in range(len(num_str)):
        if not asal_mi(int(num_str)):
            return False
        num_str = num_str[1:] + num_str[0]
    return True


sayac = 0
for num in range(2, 1000000):
    if daire_asal_mi(num):
        sayac += 1

print("1 milyona kadar dairesel asal sayıların sayısı:", sayac)
