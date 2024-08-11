import sys
input = sys.stdin.readline
import bisect

n = int(input())
li = list(map(int, input().split()))
dp = [0] * (n+1)
ans=0
for i in range(n):
    idx = li[i]
    dp[idx] = dp[idx-1] + 1
    ans = max(dp[idx], ans)

print(n-ans)