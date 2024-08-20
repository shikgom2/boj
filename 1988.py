import sys
input = sys.stdin.readline

li = []
n,k = map(int, input().split())
for _ in range(n):
    a = int(input())
    li.append(a)

# Initialize DP table with very negative numbers
dp = [[[-10] * 2 for _ in range(k + 1)] for __ in range(n + 1)]
dp[1][1][1] = li[0]  # Use val[0] for the first Xiao Ming
dp[1][0][0] = 0

# Fill DP table
for i in range(2, n + 1):
    dp[i][0][0] = dp[i-1][0][0]
    for j in range(1, k + 1):
        dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1])
        dp[i][j][1] = max(dp[i-1][j-1][0], dp[i-1][j-1][1] + li[i-1])  # Using val[i-1] here

ans = max(dp[n][k][0], dp[n][k][1])
    
print(ans)