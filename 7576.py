import sys
input = sys.stdin.readline
from collections import deque

def bfs(check, graph, visited):
    global left
    q = deque()

    for i in range(len(check)):
        q.append((check[i][0], check[i][1], 0))
        visited[check[i][0]][check[i][1]] = True
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    e = n
    v = m

    mt = 0
    while q:
        x,y,t = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if nx == -1 or nx == e or ny == -1 or ny == v:
                continue
            if(graph[nx][ny] == -1):
                continue
            if graph[nx][ny] == 0 and not visited[nx][ny]:
                #print("APPEND", n)
                q.append((nx,ny,t+1))
                mt = t+1
                visited[nx][ny] = True
                left -= 1
    
    if(left == 0):
        return mt
    else:
        return -1

graph = []
m,n = map(int, input().split())
for _ in range(n):
    l = list(map(int, input().split()))
    graph.append(l)


visited = [[False] * m for _ in range(n)]
left = 0
ans = 0
check = []
for i in range(n):
    for j in range(m):
        if(graph[i][j] == 1):
            check.append((i,j))
        elif(graph[i][j] == 0):
            left += 1

print(bfs(check, graph, visited))