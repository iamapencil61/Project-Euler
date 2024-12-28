import 'dart:math';

class PrimePower {
  final int p;
  final int r;
  PrimePower(this.p, this.r);
}

typedef VecInt = List<int>;
typedef VecLong = List<int>;
typedef IntPair = List<int>;
typedef PrimeFactors = List<int>;
typedef PrimeFactorisation = List<PrimePower>;

const int N = 1e9.toInt();
const int N_2 = N ~/ 2;
const int M = 1e9.toInt() + 7;

int SQ(int x) => (x * x) % M;

int INT(double x) => x.toInt();

int kMax = INT(N_2 / sqrt(3));

List<int> smallestPrimeFactor = List.filled(kMax + 1, 0);

PrimeFactorisation makePrimeFactorisation(int n) {
  final pf = <PrimePower>[];
  while (n > 1) {
    int p = smallestPrimeFactor[n];
    if (p == 0) {
      pf.add(PrimePower(n, 1));
      return pf;
    }
    int r = 0;
    while (n % p == 0) {
      n ~/= p;
      r++;
    }
    pf.add(PrimePower(p, r));
  }
  return pf;
}

PrimeFactors makePrimeFactors(PrimeFactorisation primeFactorisation) {
  return primeFactorisation.map((pp) => pp.p).toList();
}

int intPow(int x, int p) {
  if (p == 0) return 1;
  if (p == 1) return x;

  int tmp = intPow(x, p ~/ 2);
  if ((p % 2) == 0) {
    return tmp * tmp;
  } else {
    return x * tmp * tmp;
  }
}

void buildKIProd(int k, int l, PrimeFactorisation pf, int K_I, int prod) {
  int K_J = 1, L_J = 1, n = l;
  for (var pp in pf) {
    if (pp.r == 1) continue;
    int s = 0;
    while (n % pp.p == 0) {
      n ~/= pp.p;
      s++;
    }
    if (s < pp.r - 1) {
      K_J *= intPow(pp.p, pp.r);
      L_J *= intPow(pp.p, s);
      prod *= 2 * (s + 1);
    }
  }
  K_I = k * l ~/ (K_J * L_J);
}

int totient(int m, PrimeFactors primeFactors) {
  if (m == 1) return 1;
  int tot = m;
  for (int p in primeFactors) {
    tot ~/= p;
    tot *= (p - 1);
  }
  return tot;
}

int phi(int m, int n, PrimeFactors primeFactors) {
  if (m == 1) {
    return n;
  } else if (n <= 1) {
    return n;
  } else if (n % m == 0) {
    return (n ~/ m) * totient(m, primeFactors);
  }
  int res = n;
  for (int i = 1; i < (1 << primeFactors.length); ++i) {
    int k = i.bitCount;
    int denom = 1;
    for (int j = 0; (1 << j) <= i; ++j) {
      if ((i & (1 << j)) != 0) {
        denom *= primeFactors[j];
      }
    }
    res += (1 - 2 * (k % 2)) * (n ~/ denom);
  }
  return res;
}

int sumOfDiv(int n) {
  int res = 0;
  int sqrtNFloor = sqrt(n).toInt();
  for (int m = 1; m <= sqrtNFloor; ++m) {
    res += n ~/ m;
    res %= M;
  }
  res *= 2;
  res %= M;
  res -= sqrtNFloor * sqrtNFloor;
  res %= M;
  if (res < 0) {
    res += M;
  }
  return res;
}

void main() {
  print("Building smallest prime factor sieve");

  smallestPrimeFactor[0] = 1;
  smallestPrimeFactor[1] = 1;
  for (int p = 2; p <= kMax; ++p) {
    if (smallestPrimeFactor[p] != 0) continue;
    for (int m = 2; m * p <= kMax; ++m) {
      smallestPrimeFactor[m * p] = p;
    }
  }

  print("Building number of divisors");
  List<int> ndiv = List.filled(kMax + 1, 2);
  ndiv[0] = 0;
  ndiv[1] = 1;
  for (int n = 2; n <= sqrt(kMax).toInt(); ++n) {
    ndiv[n * n]++;
    for (int m = n + 1; m <= kMax ~/ n; ++m) {
      ndiv[m * n] += 2;
    }
  }

  int res1 = sumOfDiv(N_2);

  print("Result: $res1");
}
