import sys
input = sys.stdin.readline

def solve(s, m):
    length = min(len(s), m)
    ans = sum(int(s[i]) ** 2 for i in range(length))
    return ans

n, l, k, m = map(int, input().split())
a = []
for _ in range(n + 1):
    a.append(int(input().strip()))

mod = 10 ** m

h = [[0] * 15 for _ in range(15)]

for i in range(min(n + 1, k)):
    res = a[0]
    for j in range(1, n + 1):
        res = res * l
        res = res + a[j]
    res = res % mod
    l += 1
    h[0][i] = res
    print(solve(str(res), m))

if k > n + 1:
    for i in range(1, n + 1):
        for j in range(n - i + 1):
            h[i][j] = h[i - 1][j + 1] - h[i - 1][j]

pre = [0] * 15
for i in range(n + 1):
    pre[i] = h[i][n - i]

for i in range(n + 1, k):
    res = h[n][0]
    for j in range(n - 1, -1, -1):
        res = pre[j] + res
        res = res % mod
        pre[j] = res
    print(solve(str(res), m))