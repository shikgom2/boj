INF = 2e9

n, m = map(int, input().split())
s = [0] * (n + 1)
p = [0] * (m + 1)
dp = [[-INF] * (m+ 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    s[i], p[i] = map(int, input().split())

dp[0][0] = 0

for i in range(1, n + 1):
    for j in range(m, -1, -1):
        if (j >= p[i] + 1 and dp[i - 1][j - (p[i] + 1)] != -INF):
            dp[i][j] = max(dp[i][j], dp[i - 1][j - (p[i] + 1)] + s[i])
        if (j >= p[i] and dp[i - 1][j - p[i]] != -INF):
            dp[i][j] = max(dp[i][j], dp[i - 1][j - p[i]])
        if(dp[i - 1][j] != -INF):
            dp[i][j] = max(dp[i][j], dp[i - 1][j] - s[i])

ans = -INF
for i in range(m + 1):
    ans = max(ans, dp[n][i])

if(ans > 0):
    print('W')
elif(ans == 0):
    print('D')
else:
    print('L')