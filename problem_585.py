import numpy as np
from math import gcd


def calculate_sum1(N):
    sum1 = np.zeros(N + 1, dtype=int)
    for k1 in range(1, N + 1):
        sum1[k1] = (k1 - 1) // 2

    for k1 in range(1, int((N // 2) ** 0.5) + 1):
        for k2 in range(k1 + 1, int((N - k1 ** 2) ** 0.5) + 1):
            if gcd(k1, k2) == 1:
                s = k1 ** 2 + k2 ** 2
                m = s
                k3 = 1
                while m <= N:
                    sum1[m] -= 1
                    k3 += 1
                    m += s

    result1 = sum1.sum()
    return sum1, result1


def calculate_mobius_and_primes(N):
    mu = np.ones(N + 1, dtype=int)
    primes = np.ones(N + 1, dtype=bool)

    for k1 in range(2, int(N ** 0.5) + 1):
        if primes[k1]:
            for k2 in range(k1, N + 1, k1):
                mu[k2] *= -1
                primes[k2] = False
            primes[k1] = True
            for k2 in range(k1 * k1, N + 1, k1 * k1):
                mu[k2] = 0

    for k1 in range(int(N ** 0.5) + 1, N + 1):
        if primes[k1]:
            for k2 in range(k1, N + 1, k1):
                mu[k2] *= -1

    return mu


def calculate_sum2(N, sum1, mu):
    sum2 = sum1.copy()
    for k1 in range(2, N + 1):
        if mu[k1]:
            for k2 in range(1, N // k1 + 1):
                sum2[k1 * k2] += sum1[k2] * mu[k1]
    return sum2


def calculate_result2(N, sum1, sum2, mu):
    result2 = 0

    for k1 in range(1, N + 1):
        for k2 in range(1, N // k1 + 1):
            result2 += sum1[k1] * sum2[k2]

    for s1 in range(1, int(N ** 0.5) + 1):
        if mu[s1]:
            for s4 in range(1, N // (s1 * (s1 + s4)) + 1):
                if mu[s4] and gcd(s1, s4) == 1:
                    for t1 in range(1, N // ((s1 * t1 + s4) * (s1 * s4 + t1)) + 1):
                        if mu[t1] and gcd(t1, s1 * s4) == 1:
                            for t4 in range(1, N // ((s1 * t1 + s4 * t4) * (s1 * s4 + t1 * t4)) + 1):
                                if mu[t4] and gcd(t4, t1 * s1 * s4) == 1:
                                    if s1 == t1 == s4 == t4 == 1:
                                        continue

                                    for r in range(1, N // ((s1 * t1 + s4 * t4) * (s1 * s4 + t1 * t4)) + 1):
                                        if mu[r] and gcd(r, s1 * t1 * s4 * t4) == 1:
                                            for y in range(1, N):
                                                k2 = s1 * s4 * y * y
                                                if (k2 + t1 * t4) * (s1 * t1 + s4 * t4) * r > N:
                                                    break
                                                for z in range(1, N):
                                                    k3 = t1 * t4 * z * z
                                                    if (k2 + k3) * (s1 * t1 + s4 * t4) * r > N:
                                                        break
                                                    if k2 >= k3:
                                                        continue
                                                    if gcd(k2, k3) != 1:
                                                        continue
                                                    for x in range(1, N):
                                                        k1 = s1 * t1 * r * x * x
                                                        if (k2 + k3) * (k1 + s4 * t4 * r) > N:
                                                            break
                                                        for w in range(1, N):
                                                            k4 = s4 * t4 * r * w * w
                                                            if (k2 + k3) * (k1 + k4) > N:
                                                                break
                                                            if k1 > k4:
                                                                result2 -= 1
    return result2


def main():
    N = 5000000
    print("Calculating sum1...")
    sum1, result1 = calculate_sum1(N)

    print("Calculating Möbius function...")
    mu = calculate_mobius_and_primes(N)

    print("Calculating sum2...")
    sum2 = calculate_sum2(N, sum1, mu)

    print("Calculating result2...")
    result2 = calculate_result2(N, sum1, sum2, mu)

    print(result1 + result2 // 2)


if __name__ == "__main__":
    main()
