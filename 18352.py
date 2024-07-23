import sys
input = sys.stdin.readline
from collections import deque

def bfs(x):
    q = deque([(x, 0)])
    visited[x] = True
    while q:
        v, t = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append((i, t+1))
                visited[i] = True
                checked[i] = t+1

v, e, k, x = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(e)]
visited = [False] * (v+1)
checked = [0] * (v+1)
graph = [[] for _ in range(v + 1)]
for i, j in edges:
    graph[i].append(j)

bfs(x)

ans = []
for i in range(1, v+1):
    if(checked[i] == k):
        ans.append(i)

if(len(ans)):
    for i in range(len(ans)):
        print(ans[i])
else:
    print(-1)