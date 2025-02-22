import math
from collections import namedtuple

PrimePower = namedtuple('PrimePower', ['p', 'r'])

N = int(1e9)
N_2 = N // 2
M = int(1e9) + 7

kMax = int(N_2 / math.sqrt(3))

smallest_prime_factor = [0] * (kMax + 1)


def sq(x):
    return (x * x) % M


def int_pow(x, p):
    if p == 0:
        return 1
    if p == 1:
        return x

    tmp = int_pow(x, p // 2)
    if (p % 2) == 0:
        return tmp * tmp
    else:
        return x * tmp * tmp


# Generate prime factorization
def make_prime_factorisation(n):
    pf = []
    while n > 1:
        p = smallest_prime_factor[n]
        if p == 0:
            pf.append(PrimePower(n, 1))
            return pf
        r = 0
        while n % p == 0:
            n //= p
            r += 1
        pf.append(PrimePower(p, r))
    return pf


def make_prime_factors(prime_factorisation):
    return [pp.p for pp in prime_factorisation]


def build_ki_prod(k, l, pf, K_I, prod):
    K_J = 1
    L_J = 1
    n = l
    for pp in pf:
        if pp.r == 1:
            continue
        s = 0
        while n % pp.p == 0:
            n //= pp.p
            s += 1
        if s < pp.r - 1:
            K_J *= int_pow(pp.p, pp.r)
            L_J *= int_pow(pp.p, s)
            prod *= 2 * (s + 1)
    K_I = k * l // (K_J * L_J)


def totient(m, prime_factors):
    if m == 1:
        return 1
    tot = m
    for p in prime_factors:
        tot //= p
        tot *= (p - 1)
    return tot


def phi(m, n, prime_factors):
    if m == 1:
        return n
    elif n <= 1:
        return n
    elif n % m == 0:
        return (n // m) * totient(m, prime_factors)
    res = n
    for i in range(1, 1 << len(prime_factors)):
        k = bin(i).count('1')
        denom = 1
        for j in range(len(prime_factors)):
            if (i & (1 << j)) != 0:
                denom *= prime_factors[j]
        res += (1 - 2 * (k % 2)) * (n // denom)
    return res


def sum_of_div(n):
    res = 0
    sqrt_n_floor = int(math.sqrt(n))
    for m in range(1, sqrt_n_floor + 1):
        res += n // m
        res %= M
    res *= 2
    res %= M
    res -= sqrt_n_floor * sqrt_n_floor
    res %= M
    if res < 0:
        res += M
    return res


if __name__ == "__main__":
    print("Building smallest prime factor sieve")

    smallest_prime_factor[0] = 1
    smallest_prime_factor[1] = 1
    for p in range(2, kMax + 1):
        if smallest_prime_factor[p] != 0:
            continue
        for m in range(2, (kMax // p) + 1):
            smallest_prime_factor[m * p] = p

    print("Building number of divisors")
    ndiv = [2] * (kMax + 1)
    ndiv[0] = 0
    ndiv[1] = 1
    for n in range(2, int(math.sqrt(kMax)) + 1):
        ndiv[n * n] += 1
        for m in range(n + 1, (kMax // n) + 1):
            ndiv[m * n] += 2

    res1 = sum_of_div(N_2)

    print("Result:", res1)