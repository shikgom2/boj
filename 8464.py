import sys
input = sys.stdin.readline

def check(N):
    ans = 0
    i = 1
    while i * i <= N:
        ans += mobius[i] * (N // (i * i))
        i += 1
    return N - ans

mobius = [1] * (1000001)
for i in range(2, int(1000000**0.5) + 1):
    if mobius[i] == 1:
        for j in range(i, 1000001, i):
            mobius[j] *= -i
        for j in range(i * i, 1000001, i * i):
            mobius[j] = 0
for i in range(2, 1000001):
    if mobius[i] == i:
        mobius[i] = 1
    elif mobius[i] == -i:
        mobius[i] = -1
    elif mobius[i] < 0:
        mobius[i] = 1
    elif mobius[i] > 0:
        mobius[i] = -1

k = int(input())
lo = 0
hi = 10**12
while lo + 1 < hi:
    mid = (lo + hi) // 2
    if check(mid) < k:
        lo = mid
    else:
        hi = mid
print(hi)
