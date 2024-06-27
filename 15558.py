import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y, graph, visited):
    q = deque()
    q.append((x, y, 0))
    visited[x][y] = True
    directions = [(0, -1), (0, 1), (1, k), (-1, k)]
    e = len(graph)
    v = len(graph[0])

    while q:
        x, y, t = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            #print(nx, ny)
        
            if(ny > v-1):
                print(1)
                exit()
            
            if nx < 0 or nx >= e or ny < 0 or ny >= v:
                continue
        
            if(t >= ny):
                continue

            if (graph[nx][ny] == 1 and not visited[nx][ny]):
                q.append((nx, ny, t+1))
                visited[nx][ny] = True
    print(0)
    exit()

n, k = map(int, input().split())
graph = []
for _ in range(2):
    li = list(map(int, input().rstrip()))
    graph.append(li)

visited = [[False] * len(graph[0]) for _ in range(len(graph))]

bfs(0, 0, graph, visited)