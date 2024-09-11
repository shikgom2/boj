import sys
input = sys.stdin.readline
sys.setrecursionlimit(155557)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y):
    if dp[x][y] != -1:
        return dp[x][y]
    
    res = 0
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]

        if not 0 <= next_x < n or not 0 <= next_y < m:
            continue
        if graph[next_x][next_y] >= graph[x][y]:
            continue
        res += dfs(next_x, next_y)
    
    dp[x][y] = res
    return dp[x][y]

n,m = map(int, input().split())
graph = []

for _ in range(n):
    li = list(map(int, input().split()))
    graph.append(li)

dp = [[-1] * m for _ in range(n)]
dp[n-1][m-1] = 1
ans = dfs(0, 0)
print(ans)