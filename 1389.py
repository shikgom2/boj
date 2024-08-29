import sys
input = sys.stdin.readline
from collections import deque

def bfs(x):
    q = deque([(x,0)])
    visited[x] = 0
    while q:
        v,t = q.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                q.append((i, t+1))
                visited[i] = t+1

    return sum(visited) - visited[x]

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

ans = 10**10
idx = 0
for i in range(1, n+1):
    visited = [0] * (n+1)
    
    tmp = bfs(i)
    if(tmp < ans):
        ans = tmp
        idx = i
print(idx)