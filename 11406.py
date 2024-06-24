import sys
from collections import deque

INF = float('inf')

def add_edge(u, v, cap, cost):
    graph[u].append(v)
    graph[v].append(u)
    capacity[u][v] = cap
    cost_graph[u][v] = cost
    cost_graph[v][u] = -cost

def spfa(source, sink):
    global dist, predecessor
    dist = [INF] * (MAX)
    dist[source] = 0
    in_queue = [False] * (MAX)
    in_queue[source] = True
    queue = deque([source])
    
    while queue:
        u = queue.popleft()
        in_queue[u] = False
        for v in graph[u]:
            if capacity[u][v] > 0 and dist[v] > dist[u] + cost_graph[u][v]:
                dist[v] = dist[u] + cost_graph[u][v]
                predecessor[v] = u
                if not in_queue[v]:
                    queue.append(v)
                    in_queue[v] = True
    return dist[sink] != INF

def mcmf(source, sink):
    max_flow = 0
    min_cost = 0
    while spfa(source, sink):
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
            min_cost += flow * cost_graph[u][v]
            v = u
        
        max_flow += flow
    
    return max_flow, min_cost

n, m = map(int, input().split())

MAX = n + m + 2

graph = [[] for _ in range(MAX)]
capacity = [[0] * MAX for _ in range(MAX)]
cost_graph = [[0] * MAX for _ in range(MAX)]
dist = [0] * MAX
predecessor = [0] * MAX

source = 0
sink = n + m + 1

li1 = list(map(int, input().split())) # n

for i in range(n):
    add_edge(i + m + 1, sink, li1[i], 0) #cap, cost
    

li2 = list(map(int, input().split())) # m 

for i in range(m):
    add_edge(source, i + 1, li2[i], 0)

cap = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
cost = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

for i in range(1, m + 1):
    li = list(map(int, input().split()))
    for j in range(len(li)):
        cap[i][j + 1] = li[j]

for i in range(1, m + 1):
    for j in range(1, n + 1):
        add_edge(i, j + m, cap[i][j], 10**10)

max_flow, min_cost = mcmf(source, sink)
print(max_flow)
#print(min_cost)
