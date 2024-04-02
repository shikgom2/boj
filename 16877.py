import sys
input = sys.stdin.readline

dp = [0] * 34
dp[1] = 1

for i in range(2, 34):
    dp[i] = dp[i - 1] + dp[i - 2]

g = [0] * 3000001
g[1] = 1
g[2] = 2
g[3] = 3

for i in range(4, 3000001):
    check = [False] * 16

    for j in range(2, 34):
        if dp[j] <= i:
            check[g[i - dp[j]]] = True
    for k in range(16):
        if not check[k]:
            g[i] = k
            break

result = 0

n = int(input())
li = list(map(int, input().split()))

for l in li:
    result ^= g[l]

print("koosaga" if result != 0 else "cubelover")