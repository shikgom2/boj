N, S, M = map(int, input().split())
li = list(map(int, input().split()))

dp = [[False] * (M + 1) for _ in range(N + 1)]
dp[0][S] = True

for i in range(1, N + 1):
    diff = li[i - 1]
    for vol in range(M + 1):
        if dp[i - 1][vol]:
            if vol + diff <= M:
                dp[i][vol + diff] = True
            if vol - diff >= 0:
                dp[i][vol - diff] = True

ans = -1
for vol in range(M, -1, -1):
    if dp[N][vol]:
        ans = vol
        break

print(ans)
