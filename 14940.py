import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y, li, visited):
    q = deque()
    q.append((x, y, 0))
    visited[x][y] = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    e = len(li)
    v = len(li[0])
    
    while q:
        x, y, t = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= e or ny < 0 or ny >= v:
                continue

            if li[nx][ny] == 1 and not visited[nx][ny]:
                q.append((nx, ny, t+1))
                visited[nx][ny] = t+1
    return visited

n,m = map(int, input().split())
li = []
for _ in range(n):
    l = list(map(int, input().split()))
    li.append(l)

ans = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if(li[i][j] == 2):
            ans = bfs(i, j, li, ans)

for i in range(n):
    for j in range(m):
        if(ans[i][j] == 0):
            if(li[i][j] == 0 or li[i][j] == 2):
                print(0, end=' ')
            else:
                print(-1, end=" ")
        else:
            print(ans[i][j], end=" ")
    print()
