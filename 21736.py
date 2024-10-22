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
    
    ans = 0
    
    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= e or ny < 0 or ny >= v:
                continue
            
            if li[nx][ny] == 'O' and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True
            elif(li[nx][ny] == 'P' and not visited[nx][ny]):
                q.append((nx,ny))
                visited[nx][ny] = True
                ans += 1            
    return ans
  
n, m = map(int, input().split())
graph = []

for _ in range(n):
    li = list(map(str, input().rstrip()))
    graph.append(li)

visited = [[False] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if(graph[i][j] == 'I'):
            ans = bfs(i,j, graph, visited)
if(ans):
    print(ans)
else:
    print("TT")