import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y, li, visited):
    q = deque()
    q.append((x, y, 0))
    visited[x][y] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    e = len(li)
    v = len(li[0])
    
    ans = 1
    while q:
        x, y, z = q.popleft()
        #print((x,y,z))
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx > 1000 or ny < 0 or ny > 1000:
                continue

            if graph[nx][ny] == 0 and not visited[nx][ny]:
                q.append((nx, ny, z+1))
                visited[nx][ny] = True

            if(nx == t and ny == u):
                print(z+1)
                exit()

t, u, n = map(int, input().split())
graph = [[0] * 1001 for _ in range(1001)]

t += 500
u += 500
for _ in range(n):
    a, b = map(int, input().split())
    graph[a+500][b+500] = 1

visited = [[False] * 1001 for _ in range(1001)]

bfs(500, 500, graph, visited)