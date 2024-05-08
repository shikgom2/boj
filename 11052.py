import sys
input = sys.stdin.readline

n = int(input())
li = [0] + list(map(int, input().split()))
dp = [0] * (n+1)

dp[1] = li[1]
dp[2] = max(li[2], dp[1] + li[1])

for i in range(3, n+1):
    dp[i] = li[i]

    for j in range(1, i//2 + 1):
        dp[i] = max(dp[i], dp[j] + dp[i-j])

#print(dp)
print(dp[n])
