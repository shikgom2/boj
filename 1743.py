import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y, li, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    e = len(li)
    v = len(li[0])
    
    ans = 1
    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= e or ny < 0 or ny >= v:
                continue

            if li[nx][ny] and not visited[nx][ny] and li[nx][ny] == '#':
                q.append((nx, ny))
                ans += 1
                visited[nx][ny] = True
    return ans
                
i,j,k = map(int, input().split())

li = [[['.'] for _ in range(j)] for _ in range(i)]

for _ in range(k):
    a,b = map(int, input().split())
    li[a-1][b-1] = '#'

visited = [[False] * len(li[0]) for _ in range(len(li))]

ans = 0
for i in range(len(li)):
    for j in range(len(li[0])):
        if li[i][j] and not visited[i][j] and li[i][j] == '#':
		        ans = max(ans, bfs(i, j, li, visited))
                  
print(ans)