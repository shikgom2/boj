import sys
input = sys.stdin.readline
from collections import deque
#bfs each time and simulate dsu

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    pNum1 = find(a)
    pNum2 = find(b)
    if pNum1 == pNum2:
        return False
    parent[pNum1] = pNum2
    return True

n,m = map(int, input().split())

visited = [[False] * n for _ in range(n)]
parent = [i for i in range(m + 1)]

graph = [[0] * n for _ in range(n)]
q1 = deque()
q2 = deque()

for i in range(m):
    a, b =map(int, input().split())
    graph[a-1][b-1] = (i+1)
    q1.append((a-1,b-1))

ans = 0
cur_civil = m

directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

while True:
    # Civilization merging
    qSize = len(q1)
    for _ in range(qSize):
        x, y = q1.popleft()
        q2.append((x, y))
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] != 0:
                if union(graph[x][y], graph[nx][ny]):
                    cur_civil -= 1

    if cur_civil == 1:
        break

    # Civilization spreading
    qSize = len(q2)
    for _ in range(qSize):
        x, y = q2.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
                q1.append((nx, ny))
                graph[nx][ny] = graph[x][y]

    ans += 1
print(ans)