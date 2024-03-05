V, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]
visited = [False] * (V+1)

def dfs(x):
    visited[x] = True

    for node in graph[x]:
        if not visited[node]:
            dfs(node)

graph = [[] for _ in range(V + 1)]
for i, j in edges:
    graph[i].append(j)
    graph[j].append(i)

cnt = 0
for i in range(1, (V+1)):
    if visited[i] == False:
        dfs(i)
        cnt +=1 
print(cnt)