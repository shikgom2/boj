import sys
input = sys.stdin.readline
mod = 10007

def check(n, k, dp):
    if dp[n][k] != 0:
        return dp[n][k]
    elif k == 0 or k == n:
        dp[n][k] = 1
    else:
        dp[n][k] = (check(n - 1, k - 1, dp) + check(n - 1, k, dp)) % mod
    return dp[n][k]

n = int(input())
ans = 0
dp = [[0] * 53 for _ in range(53)]

for i in range(1, n // 4 + 1):
    if i % 2 == 1:
        ans += (check(13, i, dp) * check(52 - i * 4, n - i * 4, dp)) % mod
        ans = ans % mod
    else:
        ans -= (check(13, i, dp) * check(52 - i * 4, n - i * 4, dp)) % mod
        ans = (ans + mod) % mod

print(ans)
