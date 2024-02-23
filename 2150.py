#DFS
def dfs(graph, v, visited, stack):
    visited[v] = True
    for w in graph[v]:
        if not visited[w]:
            dfs(graph, w, visited, stack)
    stack.append(v)

#Reverse DFS
def reverseDFS(graph, v, visited, component):
    visited[v] = True
    component.append(v) #Add SCC
    for w in graph[v]:
        if not visited[w]:
            reverseDFS(graph, w, visited, component)

#input
V, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]

graph = [[] for _ in range(V + 1)]
reverse_graph = [[] for _ in range(V + 1)]
#Init graph
for i, j in edges:
    graph[i].append(j)
    reverse_graph[j].append(i)

visited = [False] * (V + 1)
stack = [] #DFS stack

# DFS on original graph
for i in range(1, V + 1):
    if not visited[i]:
        dfs(graph, i, visited, stack)

visited = [False] * (V + 1)
results = []

# Reverse DFS on reversed graph
while stack:
    node = stack.pop()
    if not visited[node]:
        component = []
        reverseDFS(reverse_graph, node, visited, component)
        results.append(sorted(component))

#Output
print(len(results))
for result in sorted(results):
    for V in result:
        print(V, end=' ')
    print('-1')