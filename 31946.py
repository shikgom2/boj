import sys
input = sys.stdin.readline
from collections import deque

from collections import deque

def bfs(x, y, li, visited, cur, jump, n, m):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    directions = [(i, j) for i in range(-jump, jump+1) for j in range(-jump, jump+1) if abs(i) + abs(j) <= jump]

    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if li[nx][ny] == cur and not visited[nx][ny]:
                    if nx == n-1 and ny == m-1:
                        return True
                    q.append((nx, ny))
                    visited[nx][ny] = True
    return False

n = int(input().strip())
m = int(input().strip())
maps = [list(map(int, input().split())) for _ in range(n)]
jump = int(input().strip())

visited = [[False] * m for _ in range(n)]
cur = maps[0][0]
if bfs(0, 0, maps, visited, cur, jump, n, m):
    print("ALIVE")
else:
    print("DEAD")
