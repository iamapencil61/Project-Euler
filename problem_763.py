import numpy as np

N = 10000
A = int(np.sqrt(2 * N))
arr = np.zeros((N, A, A), dtype=np.int64)
arr[0, 0, 0] = 1

for n in range(1, N):
    s = lambda a, b: arr[n - a - b - 1, a, b] if n >= a + b + 1 else 0
    for a in range(A):
        for b in range(A):
            c = a + b + 1
            if c * (c - 1) / 2 > n or c // 2 * c // 2 + n > N:
                break
            if a == 0:
                if b == 0:
                    res = s(0, 0) * 3 + s(1, 0) * 3
            elif a == 1:
                if b == 0:
                    res = s(0, 0) + s(1, 0) * 4 + s(2, 0) + s(1, 1) * 2
                else:
                    res = s(b, 0) + s(b + 1, 0) + s(b, 1) + s(1, b) + s(b + 1, 1) + s(1, b + 1)
            elif b == 0:
                res = s(a - 1, 0) + s(a, 0) * 2 + s(a - 1, 1) * 2 + s(a + 1, 0) + s(a, 1) * 2
            else:
                res = s(a - 1, b) + s(a, b) + s(a - 1, b + 1) + s(a + b - 1, 1) + s(a, b + 1) + s(a + b, 1)
            arr[n, a, b] = res % 1000000000

print(arr[N - 1, 0, 0])