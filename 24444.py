import sys
input = sys.stdin.readline
from collections import deque

def bfs(x):
    cur = 1
    q = deque([x])
    visited[x] = True
    while q:
        v = q.popleft()
        ans[v] = cur
        cur += 1

        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

n,m,r = map(int, input().split())
visited = [False] * (n+1)

graph = [[] for _ in range(n+1)]
ans = [0] * (n+1)

for _ in range(m):
    a,b =map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(n+1):
    graph[i].sort()

bfs(r)

for i in range(1, len(ans)):
    print(ans[i])