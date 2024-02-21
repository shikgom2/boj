import sys
sys.setrecursionlimit(10**6)

stack = []

def dfs(v, visited, stack):
    visited[v] = 1

    for w in graph[v]:
        if visited[w] == 0:
            stack.append(w)
            dfs(w, visited, stack)
    stack.append(v) 

def reverseGraph():
    reverse_graph = [[] for i in range(V+1)]
    for i in range(1, V+1):
        for j in graph[i]:
            reverse_graph[j].append(i)
    return reverse_graph

def reverseDFS(v, visited,stack):
    visited[v] = 1
    stack.append(v)
    for w in reverse_graph[v]:
        if visited[w] == 0:
            reverseDFS(w, visited, stack)

V = int(input())
E = int(input())
visited = [0] * (V+1)
graph = [[] for i in range(V + 1)]

for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)

for i in range(1, V+1):
    if visited[i] == 0:
        dfs(i, visited, stack)

reverse_graph = reverseGraph()

visited = [0] * (V+1)
results = []

while stack:
    ssc = []
    node = stack.pop()
    if visited[node] == 0:
        reverseDFS(node, visited, ssc)
        results.append(sorted(ssc))

results = sorted(results)

max = 0
for res in results:
    if(len(res) > max):
        max = len(res)
print(max)