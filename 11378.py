import sys
input = sys.stdin.readline
from collections import deque

INF = float('inf')

def add_edge(u, v, cap):
    graph[u].append(v)
    graph[v].append(u)
    capacity[u][v] = cap
    capacity[v][u] = 0
    
def bfs(source, sink):
    global predecessor
    predecessor = [-1] * (n + m + 3)
    queue = deque([source])
    predecessor[source] = source
    
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if capacity[u][v] > 0 and predecessor[v] == -1:
                predecessor[v] = u
                if v == sink:
                    return True
                queue.append(v)
    
    return False

def edmonds_karp(source, sink):
    max_flow = 0
    while bfs(source, sink):
        flow = INF
        v = sink
        
        while v != source:
            u = predecessor[v]
            flow = min(flow, capacity[u][v])
            v = u
        
        v = sink
        while v != source:
            u = predecessor[v]
            capacity[u][v] -= flow
            capacity[v][u] += flow
            v = u
        
        max_flow += flow
    
    return max_flow

n,m,k = map(int ,input().split())
graph = [[] for _ in range(n + m + 3)]
capacity = [[0] * (n + m + 3) for _ in range(n + m + 3)]

source = 0
sub = n+m+2
sink = (n+m+1)

    
can = []

for i in range(n):
    add_edge(source, (i+1), 1) #source -> human

add_edge(source, sub, k)

for i in range(n):
    add_edge(sub, (i+1), k)
        
for i in range(n):
    li = list(map(int, input().split()))
    for j in range(1, len(li)):
        add_edge(i+1, li[j] + n, 1)
        #print(f"ADD EDGE {i+1}, {li[j]+n}")

for i in range(n):
    add_edge(source, (i+1), 1)
    
for i in range(m):
    #print(f"ADD EDGE {n+i+1}, {sink}")
    add_edge(n + i + 1, sink, 1)
    
print(edmonds_karp(source, sink))