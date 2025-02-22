import math
from multiprocessing import Pool

def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

def compute_lattice_points_and_sum(args):
    c, N, M = args
    ans = 0
    for b in range(c, int(math.sqrt(N - c * c)) + 1):
        g = gcd(b, c)
        for a in range(c if c else b, int(math.sqrt(N - b * b - c * c)) + 1):
            gg = gcd(a, g)
            d = (a ^ b ^ c ^ 1) & 1
            while d <= a and d <= b and a * a + b * b + c * c + d * d <= N:
                if (((a != d and b != c) or a == b or c == d) and
                        (a * c < b * d or (a * c == b * d and a >= b)) and
                        gcd(d, gg) == 1):

                    x11 = a * a + b * b - c * c - d * d
                    x12 = 2 * (a * d + b * c)
                    x13 = 2 * (-a * c + b * d)
                    x21 = 2 * (-a * d + b * c)
                    x22 = a * a - b * b + c * c - d * d
                    x23 = 2 * (a * b + c * d)
                    x31 = 2 * (a * c + b * d)
                    x32 = 2 * (-a * b + c * d)
                    x33 = a * a - b * b - c * c + d * d

                    n = a * a + b * b + c * c + d * d

                    m1 = abs(x11) + abs(x21) + abs(x31)
                    m2 = abs(x12) + abs(x22) + abs(x32)
                    m3 = abs(x13) + abs(x23) + abs(x33)

                    m = max(m1, m2, m3)

                    if m > N:
                        d += 2
                        continue

                    g_value = gcd(x11, gcd(x12, x13)) + gcd(x21, gcd(x22, x23)) + gcd(x31, gcd(x32, x33))
                    sym = (1 if not c else
                           (6 if not d else
                            (4 if a == d else (8 if a == d and (a == b or a == c) else 24))))

                    tmp = 0
                    for k in range(1, N // m + 1):
                        tmp += ((k * n % M) ** 3 + k * (k * n + 1) * g_value + 1) % M
                        tmp *= ((N + 1 - k * m1) * (N + 1 - k * m2) % M * (N + 1 - k * m3) % M) % M

                        if tmp > (1 << 63):
                            tmp %= M

                    ans += tmp % M * sym
                    ans %= M
                d += 2
    return ans

def main():
    N = int(input("Enter N (default 5000): ") or 5000)
    M = int(input("Enter M (default 1000000000): ") or 1000000000)
    ans = 0

    with Pool() as pool:
        results = pool.map(compute_lattice_points_and_sum, [(c, N, M) for c in range(0, int(math.sqrt(N)) + 1)])
        ans = sum(results) % M

    print(ans)

if __name__ == "__main__":
    main()