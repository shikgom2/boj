import sys
input = sys.stdin.readline
import math

def dfs(u, graph, visited, match):
    for v in graph[u]:
        if not visited[v]:
            visited[v] = True
            if match[v] == -1:
                match[v] = u
                return True
            else:
                can = dfs(match[v], graph, visited, match)
                if can:
                    match[v] = u
                    return True
    return False

def can(t, n, dist):
    graph = []
    for _ in range(n):
        graph.append([])
    for i in range(n):
        for j in range(n):
            if dist[i][j] <= (t * t):
                graph[i].append(j)
    match = [-1] * n
    cnt = 0
    for i in range(n):
        visited = [False] * n
        if dfs(i, graph, visited, match):
            cnt += 1
    if cnt == n:
        return True
    else:
        return False

n = int(input())
li = []
for _ in range(n):
    x,y = map(int, input().split())
    li.append((x, y))
    
li2 = []
for _ in range(n):
    x,y = map(int, input().split())
    li2.append((x, y))
    
dist = []
high = 0.0
for i in range(n):
    sx, sy = li[i]
    row = []
    for j in range(n):
        gx, gy = li2[j]
        dx = sx - gx
        dy = sy - gy
        d2 = dx * dx + dy * dy
        row.append(d2)
        cur = math.sqrt(d2)
        if cur > high:
            high = cur
    dist.append(row)
    
lo = 0.0
hi = high

for _ in range(100):
    mid = (lo + hi) / 2.0
    if can(mid, n, dist):
        hi = mid
    else:
        lo = mid
print(hi)
