import sys
input = sys.stdin.readline

n = int(input())
li = [0] + list(map(int, input().split()))

# dp[i][j][k] = max k bits for the subarray from i to j
dp = [[[-float('inf')] * 522 for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1):
    dp[i][i][li[i]] = 1

for d in range(1, n):
    for i in range(1, n - d + 1):
        for bits in range(512):
            if dp[i][i+d-1][bits ^ li[i+d]] > 0:
                dp[i][i+d][bits] = max(dp[i][i+d][bits], dp[i][i+d-1][bits ^ li[i+d]] + 1)
            dp[i][i+d][bits] = max(dp[i][i+d][bits], dp[i][i+d-1][bits])
            dp[i][i+d][bits] = max(dp[i][i+d][bits], dp[i+1][i+d][bits])

t = int(input())
for _ in range(t):
    i, j = map(int, input().split())
    ans = 0
    for bits in range(512):
        ans = max(ans, bits + dp[i][j][bits])
    print(ans)
