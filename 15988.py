mod = 1000000009

dp = [0] * 1000001
dp[1] = 1
dp[2] = 2
dp[3] = 4
dp[4] = 7

for i in range(5, 1000001):
    dp[i] = (dp[i-3] + dp[i-2] + dp[i-1]) % mod
     
t = int(input())
for _ in range(t):
    i = int(input())
    print(dp[i])
