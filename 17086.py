import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y, li, visited):
    q = deque()
    q.append((x, y, 0))
    visited[x][y] = True
    directions = [(1,1), (-1, -1),(1,-1), (-1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)]
    e = len(li)
    v = len(li[0])

    while q:
        x, y, z = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= e or ny < 0 or ny >= v:
                continue
                        
            if li[nx][ny] == 0 and not visited[nx][ny]:
                q.append((nx, ny, z+1))
                visited[nx][ny] = True
            elif(li[nx][ny] == 1):
                return z+1

n,m = map(int, input().split())
li = []
for _ in range(n):
    s = list(map(int, input().split()))
    li.append(s)

ans = 0
for i in range(n):
    for j in range(m):
        if(li[i][j] == 0):
            visited = [[False] * len(li[0]) for _ in range(len(li))]
            ans = max(ans, bfs(i, j, li, visited))

print(ans)