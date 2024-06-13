n = int(input())
li = list(map(float, input().split()))
li2 = list(map(int, input().split()))
s = sum(li2)

dp = li2.copy()
ans = 0

for i in range(n):
    for j in range(i):
        if li[j] <= li[i]:
            dp[i] = max(dp[i], dp[j] + li2[i])
    ans = max(ans, dp[i])

print(s - ans)