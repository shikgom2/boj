import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y, li, no, visited, tx, ty):
    q = deque()
    q.append((x, y, 0))
    visited[x][y] = True
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (1, 1)]
    dir2 = [(-1, -1), (-1, 0), (0,1), (1,0), (1,-1), (0,-1)]
    e = len(li)
    v = len(li[0])
    
    while q:
        x, y, z= q.popleft()
        
        if(x == tx-1 and y == ty - 1):
            return z
        
        if(x % 2 == 0):
            for dx, dy in dir2:
                nx, ny = x + dx, y + dy

                if nx < 0 or nx >= e or ny < 0 or ny >= v:
                    continue

                if li[nx][ny] and not visited[nx][ny]:
                    q.append((nx, ny, z+1))
                    visited[nx][ny] = True
                    if(nx == tx-1 and ny == ty - 1):
                        return z+1
        else:
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if nx < 0 or nx >= e or ny < 0 or ny >= v:
                    continue

                if li[nx][ny] and not visited[nx][ny]:
                    q.append((nx, ny, z+1))
                    visited[nx][ny] = True
                    if(nx == tx-1 and ny == ty - 1):
                        return z+1
                    
    return -1

i,j,k = map(int, input().split())

li = [[1] * j for _ in range(i)]
no = []
for _ in range(k):
    x,y = map(int, input().split())
    li[x][y] = 0
    
visited = [[False] * len(li[0]) for _ in range(len(li))]

ans = bfs(0, 0, li, no, visited, i, j)
print(ans)