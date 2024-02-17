i = int(input())
dp = [0] * 1000001
dp[1] = 2
dp[2] = 7
dp[3] = 22

for n in range(4, i+1):
    dp[n] = (dp[n-1] * 3 + dp[n-2] - dp[n-3]) % 1000000007

print(dp[i])