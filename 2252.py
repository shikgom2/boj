
def dfs(node, graph, visited, stack):
    visited[node] = True

    for next in graph[node]:
        if not visited[next]:
            dfs(next, graph, visited, stack)
    
    stack.append(node)

N, M = map(int, input().split())
graph = {}

for i in range(0, N):
    graph[i] = []

for _ in range(0, M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)

visited = [False for _ in range(0, N)]
stack = []

for i in range(0, N):
    if not visited[i]:
        dfs(i, graph, visited, stack)

while stack:
    print(stack.pop() + 1, end=' ')