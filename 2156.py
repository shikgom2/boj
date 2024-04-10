n = int(input())
li = [0] * (n+1)
for i in range(1, n+1):
    li[i] = int(input())

dp = [0] * (n+1)
dp[1] = li[1]
if n >= 2:
    dp[2] = dp[1] + li[2]
for i in range(3, n+1):
    dp[i] = max(dp[i-3] + li[i] + li[i-1], dp[i-2] + li[i])
    dp[i] = max(dp[i-1], dp[i])
print(dp[n])