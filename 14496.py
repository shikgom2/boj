import sys
input = sys.stdin.readline
from collections import deque


def bfs(x, y):
    q = deque([(x, 0)])
    visited = [False] * (n + 1)
    visited[x] = True

    while q:
        v = q.popleft()
        if(y == v[0]):
            return v[1]
        for i in graph[v[0]]:
            if not visited[i]:
                q.append((i, v[1] + 1))
                visited[i] = True
    
    return -1

x, y = map(int, input().split())
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

ans1 = bfs(x, y)
ans2 = bfs(y, x)

print(min(ans1, ans2))