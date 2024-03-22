dp = [0] * 1000001
dp[0] = 0
dp[1] = 0
dp[2] = 1
i = int(input())
for a in range(3, i+1):
    dp[a] = ((a-1) * (dp[a-1] + dp[a-2])) % 10**9
print(dp[i])