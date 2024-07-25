import sys
input = sys.stdin.readline

n,m = map(int, input().split())

li = []
for _ in range(n):
    t = list(map(int, input().split()))
    li.append(t)

#dp[i][j] = (i-1) 까지 선택 + 자기선택의 최솟값

dp = [[10**10] * (m) for _ in range(n)]
for i in range(m):
    dp[0][i] = li[0][i]

for i in range(1, n): #세로
    for j in range(m): #가로
        mindp = 10**10
        for k in range(m): #가로 check
            if(j != k):
                mindp = min(dp[i-1][k], mindp)
        dp[i][j] = mindp + li[i][j]

print(min(dp[n-1]))