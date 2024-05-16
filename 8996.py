def f(x0):
    ans = 0
    for i in range(1, n):
        ans += abs(x0 * i - x[i])
    return ans

n = int(input())
x = list(map(int, input().split()))

# 삼분 탐색
lo = 0
hi = x[n-1]

while hi - lo >= 3:
    p = (lo * 2 + hi) // 3
    q = (lo + hi * 2) // 3
    if f(p) <= f(q):
        hi = q
    else:
        lo = p

result = 10**20
for i in range(lo, hi+1):
    result = min(f(i), result)

print(result)