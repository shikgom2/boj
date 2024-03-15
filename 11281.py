import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

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

# DFS
def dfs(graph, v, visited, stack):
    visited[v] = True
    for w in graph[v]:
        if not visited[w]:
            dfs(graph, w, visited, stack)
    stack.append(v)

# Reverse DFS
def reverseDFS(graph, v, visited, component):
    visited[v] = True
    component.append(v)  # Add SCC
    for w in graph[v]:
        if not visited[w]:
            reverseDFS(graph, w, visited, component)

# input

V, E = map(int, input().split())

graph = [[] for _ in range((V + 1) * 2)]
reverse_graph = [[] for _ in range((V + 1) * 2)]

for _ in range(E):
    i, j = map(int, input().split())
    add_edge(i, j)

visited = [False] * ((V + 1) * 2)
stack = []  # DFS stack

# DFS on original graph
for i in range(V * 2):
    if not visited[i]:
        dfs(graph, i, visited, stack)

visited = [False] * ((V + 1) * 2)
sccs  = []

# Reverse DFS on reversed graph
while stack:
    node = stack.pop()
    if not visited[node]:
        component = []
        reverseDFS(reverse_graph, node, visited, component)
        sccs .append(sorted(component))

var_in_scc = [0] * (V * 2)
for i, scc in enumerate(sccs):
    for v in scc:
        var_in_scc[v] = i

res = True
for i in range(V):
    if var_in_scc[i * 2] == var_in_scc[i * 2 + 1]:
        res = False
        break

if res:
    print(1)
else:
    print(0)