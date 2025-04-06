import sys
input = sys.stdin.readline

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]

INF = 10**9
dp = [INF] * (1 << n)
dp[0] = 0
for m in range(1 << n):
    i = m.bit_count()
    if i >= n:
        continue
    for j in range(n):
        if m & (1 << j) == 0:
            new_m = m | (1 << j)
            new_cost = dp[m] + cost[i][j]
            if new_cost < dp[new_m]:
                dp[new_m] = new_cost
                
print(dp[(1 << n) - 1])