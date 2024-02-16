i = int(input())

dp = [0] * (81)
dp[1] = 4
dp[2] = 6

for n in range(3, i+1):
    dp[n] = dp[n-2] + dp[n-1]

print(dp[i])