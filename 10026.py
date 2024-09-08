import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y, li, visited, cur):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    e = len(li)
    v = len(li[0])
    
    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= e or ny < 0 or ny >= v:
                continue

            if(li[nx][ny] == cur and not visited[nx][ny]):
                q.append((nx, ny))
                visited[nx][ny] = True

n = int(input())
li = []
for _ in range(n):
    s = list(map(str, input().rstrip()))
    li.append(s)

visited = [[False] * n for _ in range(n)]

ans1 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            ans1 += 1
            bfs(i,j, li, visited, li[i][j])

for i in range(n):
    for j in range(n):
        if(li[i][j] == 'R'):
            li[i][j] = 'G'

ans2 = 0
visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            ans2 += 1
            bfs(i,j, li, visited, li[i][j])

print(ans1, ans2)