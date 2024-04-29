import sys
input = sys.stdin.readline

#2_dim memo
line = [[0] * 101 for _ in range(101)]
dp = [[0] * 101 for _ in range(101)]

n = int(input())
#Input
for _ in range(n):
    a, b = map(int, input().split())
    line[a][b] = 1
    line[b][a] = 1

#DP
for i in range(1, 101):
    for j in range(i, 0, -1):
        for k in range(j, i):
            '''
            simulate
            dp[1][1] remains unchanged
            dp[2][2] remains unchanged
            dp[1][2] = max(dp[1][2], dp[1][1] + dp[1][2] + line[2][1])
            dp[3][3] remains unchanged
            dp[2][3] = max(dp[2][3], dp[2][2] + dp[2][3] + line[3][2])
            dp[1][3] = max(dp[1][3], dp[1][1] + dp[1][3] + line[3][1])
            dp[4][4] remains unchanged
            dp[3][4] = max(dp[3][4], dp[3][3] + dp[3][4] + line[4][3])
            ........
            dp[1][100] = max(dp[1][100], dp[1][99] + dp[99][100] + line[100][1])
            '''
            dp[j][i] = max(dp[j][i], dp[j][k] + dp[k][i] + line[i][j])
print(dp[1][100])


