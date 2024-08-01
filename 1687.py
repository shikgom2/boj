import sys
input = sys.stdin.readline

n,m = map(int, input().split())
graph = []

for _ in range(n):
    li = list(map(int, input().rstrip()))
    graph.append(li)

dp = [[0] * m for _ in range(n)]

for i in range(m):
    dp[0][i] = 1 if graph[0][i] == 0 else 0
    for j in range(1, n):
        dp[j][i] = dp[j-1][i] + 1 if graph[j][i] == 0 else 0

ans = 0
for i in range(n):
    stack = []
    for j in range(m):
        cnt = 1
        while stack and stack[-1][1] >= dp[i][j]:
            cnt += stack[-1][0]
            ans = max(ans, stack[-1][1] * (cnt - 1))
            stack.pop()
        stack.append((cnt, dp[i][j]))
        ans = max(ans, cnt * dp[i][j])
    
    tot = 0
    while stack:
        tot += stack[-1][0]
        ans = max(ans, tot * stack[-1][1])
        stack.pop()

print(ans)
