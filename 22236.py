import sys
input = sys.stdin.readline 

d, m = map(int, input().split())

dp = [[0] * (d + 1) for _ in range(d + 1)]
dp[0][0] = 1

for i in range(1, d + 1):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] = dp[i - 1][j + 1]
        elif j == i:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            if j - 1 == 0:
                dp[i][j] = dp[i - 1][j + 1]
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
        
        dp[i][j] %= m

print(dp[d][0])