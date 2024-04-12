import sys
input = sys.stdin.readline

n, m = map(int, input().split())
memory = [0] + list(map(int, input().split()))
cost = [0] + list(map(int, input().split()))

dp = [[0 for _ in range(10001)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(10001):
        if cost[i] > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost[i]] + memory[i])

for a in range(10001):
    if dp[n][a] >= m:
        print(a)
        break