import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def dfs(node):
    visited[node] = True
    dp[node][0] = 0
    dp[node][1] = 1
    for next in graph[node]:
        if False == visited[next]:
            dfs(next)
            dp[node][0] += dp[next][1]
            dp[node][1] += min(dp[next][0], dp[next][1])

n = int(input())
graph = [[] for _ in range(n + 1)]
dp = [[0] * 2 for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(1)
print(min(dp[1][0], dp[1][1]))