import sys
input = sys.stdin.readline

dp = [0] * 191230
dp[1] = 1
dp[2] = 2
mod = 10**9 + 7
for i in range(3, 191230):
    dp[i] = (dp[i-1] + dp[i-2]) % mod

t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n])