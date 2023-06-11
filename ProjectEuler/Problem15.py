def bulunanYollar(izgaraBuyuklugu):
    # Bir matris oluşturuyorum.
    izgara = [[0] * (izgaraBuyuklugu + 1) for x in range(izgaraBuyuklugu + 1)]

    # Başlangıç noktasını 1 olarak işaretledim.

    izgara[0][0] = 1

    # Izgarayı doldurma işlemleri

    for y in range(izgaraBuyuklugu + 1):
        for z in range(izgaraBuyuklugu + 1):
            if y > 0:
                izgara[y][z] += izgara[y - 1][z] # Sol hücreden gelinen yol sayısı
            if z > 0:
                izgara[y][z] += izgara[y][z - 1]  # Üst hücreden gelinen yol sayısı

    # Sağ alt köşeye ulaşmanın farklı yollarının sayısını döndürdüm.
    return izgara[izgaraBuyuklugu][izgaraBuyuklugu]

izgaraBuyuklugu = 20
sonuc = bulunanYollar(izgaraBuyuklugu)
print(f"Farklı yolların sayısı: {sonuc}")