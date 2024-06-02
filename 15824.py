import sys
input = sys.stdin.readline
mod = 10**9 + 7

n = int(input())
li = list(map(int, input().split()))

li.sort()

dp = [1] * (n + 1)
for i in range(1, n + 1):
    dp[i] = (dp[i - 1] * 2) % mod

ans = 0
for i in range(1, n + 1):
    ans = (ans + (dp[i - 1] - dp[n - i]) * li[i - 1]) % mod

if ans < 0:
    ans += mod

print(ans)