

def add_edge(a, b):
    if a < 0: a = (-a) * 2 - 2
    else: a = a * 2 - 1

    if b < 0: b = (-b) * 2 - 2
    else: b = b * 2 - 1

    na = a + 1 if a % 2 == 0 else a - 1
    nb = b + 1 if b % 2 == 0 else b - 1

    graph[na].append(b)
    reverse_graph[b].append(na)

    graph[nb].append(a)
    reverse_graph[a].append(nb)  

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

graph = [[] for _ in range(V * 2)]
reverse_graph = [[] for _ in range(V * 2)]

for _ in range(E):
    i, j = map(int, input().split())
    add_edge(i,j)

visited = [False] * (V * 2)
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
