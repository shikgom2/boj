import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    e = len(maps)
    v = len(maps[0])
    
    ans = 1
    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= e or ny < 0 or ny >= v:
                continue

            if maps[nx][ny]==0 and not visited[nx][ny]:
                q.append((nx, ny))
                maps[nx][ny] = 2
                visited[nx][ny] = True

n,m = map(int, input().split())

graph = []
for _ in range(n):
    li = list(map(int, input().split()))
    graph.append(li)

li = []
for i in range(n):
    for j in range(m):
        if(graph[i][j] == 0):
            li.append((i,j))
ans = 0

# n^3 make walls
for i in range(len(li)):
    for j in range(i+1, len(li)):
        for k in range(j+1, len(li)):
           
            #initalize graph
            maps = [[0] * m for _ in range(n)]
            for a in range(n):
                for b in range(m):
                    maps[a][b] = graph[a][b]

            maps[li[i][0]][li[i][1]] = 1
            maps[li[j][0]][li[j][1]] = 1
            maps[li[k][0]][li[k][1]] = 1

            visited = [[False] * m for _ in range(n)]

            #simulate
            for a in range(n):
                for b in range(m):
                    if(maps[a][b] == 2): #virus
                        bfs(a,b,visited)
            #check
            t = 0
            for a in range(n):
                for b in range(m):
                    if(maps[a][b] == 0):
                        t += 1
            ans = max(t, ans)
print(ans)