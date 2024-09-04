import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y, li, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    e = n
    v = n
    
    ans = 1
    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= e or ny < 0 or ny >= v:
                continue

            if li[nx][ny] and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True
                ans += 1
    return ans

n = int(input())
li = []

for _ in range(n):
    s = list(map(int, input().rstrip()))
    li.append(s)

ans = []

visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if(li[i][j] == 1 and visited[i][j] == False):
            ans.append(bfs(i,j, li, visited))

print(len(ans))
ans.sort()
for i in range(len(ans)):
    print(ans[i])