from collections import deque

def bfs(x):
    q = deque([x])
    visited[x] = True
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
    print(q)


V, E, K, X = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]
visited = [False] * (V+1)
graph = [[] for _ in range(V + 1)]
for i, j in edges:
    graph[i].append(j)

print(bfs(X))