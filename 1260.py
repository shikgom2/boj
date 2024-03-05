from collections import deque

V, E, n= map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]
visited = [False] * (V+1)

res1 = []
rse2 = [] 

def dfs(x):
    visited[x] = True
    print(x, end=" ")
    for node in graph[x]:
        if not visited[node]:
            dfs(node)

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

graph = [[] for _ in range(V + 1)]
for i, j in edges:
    graph[i].append(j)
    graph[j].append(i)

graph = [sorted(sublist) for sublist in graph]

dfs(n)
print()
visited = [False] * (V+1)
bfs(n)