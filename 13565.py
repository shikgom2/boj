import sys
input = sys.stdin.readline
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q = deque()
    q.append((y, x))
    visited[y][x] = True

    while q:
        a, b = q.popleft()

        for i in range(4):
            next_x = a + dx[i]
            next_y = b + dy[i]

            if 0 <= next_x < n and 0 <= next_y < m:
                if not visited[next_x][next_y] and graph[next_x][next_y] == 0:
                    visited[next_x][next_y] = True
                    q.append((next_x, next_y))

n, m = map(int, input().split())
visited = [[False] * m for _ in range(n)]

graph = []
for _ in range(n):
    li = list(map(int, input().strip()))
    graph.append(li)

for i in range(m):
    if graph[0][i] == 0 and not visited[0][i]:
        bfs(i, 0)

for i in range(m):
    if visited[n-1][i]:
        print("YES")
        exit()

print("NO")