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
visited = [0] * (V+1)
graph = [[] for i in range(V + 1)]
cost = list(map(int, input().split()))

for i in range(V):
    li = list(map(int, input().strip()))
    for j in range(0, len(li)):
        if(li[j] == 1):
            graph[i+1].append(j+1)

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
sum = 0
for res in results:
    min = 10**10
    for i in res:
        if(min > cost[i-1]):
            min = cost[i-1]
    sum += min
print(sum)