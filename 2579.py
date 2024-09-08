import sys
input = sys.stdin.readline

li = [0] * 1557
n = int(input())
for i in range(n):
    k = int(input())
    li[i] = k

dp = [0] * 1557

dp[0] = li[0]
dp[1] = li[0] + li[1]

for i in range(2, n):
    dp[i] = max(dp[i-2] + li[i], dp[i-3] + li[i-1] + li[i])

print(dp[n-1])