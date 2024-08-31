import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(a, b, length, s, dp):
    if dp[a][b] >= 0:
        return dp[a][b]
    if a == 0 or b == length:
        return 0

    dp[a][b] = 0
    dp[a][b] = max(dp[a][b], dfs(a - 1, b, length, s, dp))
    dp[a][b] = max(dp[a][b], dfs(a, b - 1, length, s, dp))
    dp[a][b] = max(dp[a][b], dfs(a - 1, b - 1, length, s, dp) + (s[a - 1] == s[b - 1]))

    return dp[a][b]

s = input().strip()
n = len(s)

dp = [[-1] * (n + 1) for _ in range(n + 1)]

ans = 0
for length in range(1, n):
    ans =  max(ans, min(length, n - length) - dfs(length, n, length, s, dp))

print(ans)
