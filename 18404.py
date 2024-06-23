import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y, visited, ans):
    q = deque()
    q.append((x, y, 1))
    visited[x][y] = True
    ans[x][y] = 1

    directions = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1,2), (2, -1), (2, 1)]
    x_max = n
    y_max = n
    while q:
        x, y, time = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if nx <= 0 or nx > x_max or ny <= 0 or ny > y_max:
                continue
            
            if not visited[nx][ny]:
                q.append((nx, ny, time+1))
                ans[nx][ny] = int(time)
                visited[nx][ny] = True

n,m = map(int, input().split())
x, y =map(int, input().split())

visited = [[False] * (n+1) for _ in range(n+1)]
ans = [[0] * (n+1) for _ in range(n+1)]

bfs(x, y, visited, ans)
#print(ans)

res = []
for _ in range(m):
    x,y = map(int, input().split())
    res.append(ans[x][y])

print(*res)
