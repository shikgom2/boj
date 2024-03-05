import sys
input = sys.stdin.readline
from collections import deque

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= E or ny < 0 or ny >= V:
                continue
            if arr[nx][ny] and not visited[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny]=True


T = int(input())
for _ in range(T):
    V,E,C = map(int, input().split())

    arr = [[0]*V for _ in range(E)]
    visited = [[False]*V for _ in range(E)]

    for i in range(C):
        y, x = map(int, input().split())
        arr[x][y] = 1
    
    cnt = 0
    for i in range(E):
        for j in range(V):
             if arr[i][j] and not visited[i][j]:
                bfs(i,j)
                cnt += 1
    print(cnt)