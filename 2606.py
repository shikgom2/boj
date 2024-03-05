import sys
input = sys.stdin.readline

def dfs(x):
    visited[x] = True

    for node in graph[x]:
        if not visited[node]:
            dfs(node)


V= int(input())
E = int(input())

edges = [list(map(int, input().split())) for _ in range(E)]
visited = [False] * (V+1)

graph = [[] for _ in range(V + 1)]
#Init graph
for i, j in edges:
    graph[i].append(j)
    graph[j].append(i)

dfs(1)
cnt = 0
for i in visited:
    if(i):
        cnt += 1
print(cnt-1)
