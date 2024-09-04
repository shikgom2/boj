import sys
input = sys.stdin.readline

N = 100
dp = [[0] * 2 for _ in range(N)]
a = [0] * N
b = [0] * N

n, k = map(int, input().split())

for i in range(N):
    if i % 2 == 0:
        b[i] = k
    else:
        b[i] = 1 
    a[i] = n % k
    n //= k

dp[N - 1][1] = 1

for i in range(N - 2, -1, -1):
    for d in range(b[i]):
        dp[i][0] += dp[i + 1][0]
        if d < a[i]:
            dp[i][0] += dp[i + 1][1]
        if d == a[i]:
            dp[i][1] += dp[i + 1][1]

print(dp[0][0] + dp[0][1])