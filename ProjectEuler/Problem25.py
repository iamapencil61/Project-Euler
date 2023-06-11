def fibonacciBasamaklari(n):
    a, b = 1, 1
    sayac = 2

    while len(str(b)) < n:
        a, b = b, a + b
        sayac += 1

    return sayac

sonuc = fibonacciBasamaklari(1000)
print("1000 basamaktan fazla olan ilk Fibonacci teriminin dizini:", sonuc)