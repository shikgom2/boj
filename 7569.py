import sys
input = sys.stdin.readline
from collections import deque

def bfs(check, graph, visited):
    global left
    q = deque()

    for i in range(len(check)):
        q.append((check[i][0], check[i][1], check[i][2], 0))
        visited[check[i][0]][check[i][1]][check[i][2]] = True
    
    directions = [(0,-1, 0), (0,1, 0), (0,0, -1), (0,0, 1), (-1,0,0), (1,0,0)]
    e = n
    v = m

    mt = 0
    while q:
        z,x,y,t = q.popleft()
        for dz, dx, dy in directions:
            nz, nx, ny = z + dz, x + dx, y + dy
            if nx == -1 or nx == e or ny == -1 or ny == v or nz == -1 or nz == h:
                continue
            if(graph[nz][nx][ny] == -1):
                continue
            if graph[nz][nx][ny] == 0 and not visited[nz][nx][ny]:
                #print("APPEND", n)
                q.append((nz,nx,ny,t+1))
                mt = t+1
                visited[nz][nx][ny] = True
                left -= 1
    
    if(left == 0):
        return mt
    else:
        return -1
    
m,n,h = map(int, input().split())
graph = [[[] for _ in range(n)] for _ in range(h)]

for k in range(h):
    for i in range(n):
        graph[k][i] = list(map(int, input().split()))

visited = [[[False] * m for _ in range(n)] for _ in range(h)]

left = 0
ans = 0
check = []
for i in range(h):
    for j in range(n):
        for k in range(m):
            if(graph[i][j][k] == 1):
                check.append((i,j,k))
            elif(graph[i][j][k] == 0):
                left += 1

print(bfs(check, graph, visited))