import 'dart:math';

void main() {
  int N = 10000;
  int A = sqrt(2 * N).toInt();

  // Çok boyutlu bir dizi oluşturuyoruz.
  var arr = List.generate(N,
          (n) => List.generate(A, (a) => List.generate(A, (b) => 0, growable: false), growable: false),
      growable: false);

  // İlk elemanı 1 olarak belirliyoruz.
  arr[0][0][0] = 1;

  // Ana döngü
  for (int n = 1; n < N; n++) {
    // Yardımcı fonksiyon: s(a, b)
    int s(int a, int b) {
      return n >= a + b + 1 ? arr[n - a - b - 1][a][b] : 0;
    }

    for (int a = 0; a < A; a++) {
      for (int b = 0; b < A; b++) {
        int c = a + b + 1;

        // Şartları kontrol ediyoruz
        if (c * (c - 1) / 2 > n || (c ~/ 2) * (c ~/ 2) + n > N) {
          break;
        }

        int res = 0;

        // Farklı durumları kontrol ederek `res` değerini hesaplıyoruz.
        if (a == 0) {
          if (b == 0) {
            res = s(0, 0) * 3 + s(1, 0) * 3;
          }
        } else if (a == 1) {
          if (b == 0) {
            res = s(0, 0) + s(1, 0) * 4 + s(2, 0) + s(1, 1) * 2;
          } else {
            res = s(b, 0) + s(b + 1, 0) + s(b, 1) + s(1, b) + s(b + 1, 1) + s(1, b + 1);
          }
        } else if (b == 0) {
          res = s(a - 1, 0) + s(a, 0) * 2 + s(a - 1, 1) * 2 + s(a + 1, 0) + s(a, 1) * 2;
        } else {
          res = s(a - 1, b) + s(a, b) + s(a - 1, b + 1) + s(a + b - 1, 1) + s(a, b + 1) + s(a + b, 1);
        }

        arr[n][a][b] = res % 1000000000;
      }
    }
  }

  // Sonucu yazdırıyoruz.
  print(arr[N - 1][0][0]);
}
