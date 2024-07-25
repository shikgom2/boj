import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y, visited):
    q = deque()
    q.append((x, y, 0))
    visited[x][y] = True
    e = 1001
    v = 1001
    while q:
        x, y, t = q.popleft()
        #case 1
        nx, ny = x * 2 , y + 3
        if not nx >= e or ny >= v:
            if(nx == ny):
                return t+1
            if not visited[nx][ny]:
                q.append((nx, ny, t+1))
                visited[nx][ny] = True
        #case 2
        nx, ny = x + 1, y
        if not nx >= e or ny >= v:
            if(nx == ny):
                return t+1
            if not visited[nx][ny]:
                q.append((nx, ny, t+1))
                visited[nx][ny] = True

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    visited = [[False] * 1001 for _ in range(1001)]

    ans = bfs(n,m, visited)
    print(ans)