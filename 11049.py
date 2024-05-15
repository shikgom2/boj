import sys
input = sys.stdin.readline
n = int(input())
li = [list(map(int, input().split())) for i in range(n)]
dp = [[0] * n for i in range(n)]

for idx in range(n-1):
    for i in range(n-1-idx):
        j = i + idx +1
        dp[i][j] = 2**40
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + li[i][0] * li[k][1] * li[j][1])

print(dp[0][-1])