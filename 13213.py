import sys
input = sys.stdin.readline
from collections import deque

def bfs(N, graph):
    dist = [[0, 0] for _ in range(N)]
    dist[0][0] = dist[0][1] = 1
    que = deque([(0, 0), (0, 1)])
    
    while que:
        x, w = que.popleft()
        for nxt in graph[x][w]:
            if dist[nxt][w ^ 1]:
                continue
            dist[nxt][w ^ 1] = dist[x][w] + 1
            que.append((nxt, w ^ 1))
    
    return dist

N, E = map(int, input().split())

graph = [[[] for _ in range(2)] for _ in range(N)]

for _ in range(E):
    x, y, w = map(int, input().split())
    graph[x][w].append(y)
    graph[y][w].append(x)

dist = bfs(N, graph)

ans1 = dist[N - 1][0]
ans2 = dist[N - 1][1]

if ans1 and ans2:
    print(min(ans1, ans2) - 1)
elif ans1:
    print(ans1 - 1)
elif ans2:
    print(ans2 - 1)
else:
    print(-1)