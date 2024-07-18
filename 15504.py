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

n = int(input())
m = n

graph = [[] for _ in range(n + m + 2)]
capacity = [[0] * (n + m + 2) for _ in range(n + m + 2)]
cost_graph = [[0] * (n + m + 2) for _ in range(n + m + 2)]
dist = [0] * (n + m + 2)
predecessor = [0] * (n + m + 2)

source = 0
sink = n + m + 1

li1 = list(map(int, input().split())) #실력 
li2 = list(map(int, input().split())) #흥미로움
li3 = list(map(int, input().split())) #최대경기수

li = []
for i in range(n):
    li.append((li1[i], li2[i], li3[i]))

li.sort(key=lambda x : x[0])

#i->j
for i in range(n - 1, -1, -1):
    for j in range(i - 1, -1, -1):
        add_edge(i + 1, j + n + 1, 1, (li[i][0] ^ li[j][0]) * -1)

    #source -> i
    add_edge(source, i + 1, li[i][2] - (0 if i == n - 1 else 1), li[i][1])

    #j -> sink
    add_edge(i + n + 1, sink, 1, li[i][1])

max_flow, min_cost = mcmf(source, sink)

print(min_cost * -1)