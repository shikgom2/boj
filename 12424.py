import sys
input = sys.stdin.readline
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
    dist = [INF] * (n + m + 2)
    dist[source] = 0
    in_queue = [False] * (n + m + 2)
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

t = int(input())
for ttt in range(t):
    n = 3
    m = 3

    graph = [[] for _ in range(n + m + 3)]
    capacity = [[0] * (n + m + 2) for _ in range(n + m + 2)]
    cost_graph = [[0] * (n + m + 2) for _ in range(n + m + 2)]
    dist = [0] * (n + m + 2)
    predecessor = [0] * (n + m + 2)

    source = 0
    sink = n + m + 1

    li = list(map(int, input().split()))
    
    #n -> m
    for i in range(3):
        arr = list(map(int, input().split()))
        for j in range(3):
            add_edge(i+1, n + j + 1, min(li[i+1], li[n+j+1]), -arr[j])  #s, e, cap, cost
            #print(i+1, "->", n+j+1,  min(li[i+1], li[n+j+1]), -arr[j])

    #source -> n
    for i in range(1, n + 1):
        #사람이없다면 간선 capcity 0        
        add_edge(source, i, li[i], 0)

    #m -> sinks
    for j in range(1, m + 1):
        #사람이없다면 간선 capcity 0
        add_edge(n + j, sink, li[n + j], 0)

    max_flow, min_cost = mcmf(source, sink)

    #print(max_flow)
    ttt += 1
    print(f"Case #{ttt}:",min_cost*-1)