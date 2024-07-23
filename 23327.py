import sys
input = sys.stdin.readline

n,m = map(int, input().split())
li = list(map(int, input().split()))
dp = [0] * (n + 1)
for i in range(1, n + 1):
    dp[i] = dp[i - 1] + li[i - 1]

ans = [0] * (n + 1)
for i in range(1, n + 1):
    ans[i] = ans[i - 1] + dp[i - 1] * (dp[i] - dp[i - 1])

for _ in range(m):
    s, e = map(int, input().split())
    if s == 1:
        print(ans[e])
    else:
        print(ans[e] - (dp[e] - dp[s - 1]) * dp[s - 1] - ans[s - 1])