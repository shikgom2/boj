import sys
import math
from collections import deque
input = sys.stdin.readline
INF = float('inf')

def add_edge(u, v, cap, cost):
    graph[u].append(v)
    graph[v].append(u)
    capacity[u][v] = cap
    cost_graph[u][v] = cost
    cost_graph[v][u] = -cost

def spfa(source, sink):
    global dist, predecessor
    dist = [INF] * total
    predecessor = [-1] * total
    in_queue = [False] * total
    dist[source] = 0
    in_queue[source] = True
    dq = deque([source])
    while dq:
        u = dq.popleft()
        in_queue[u] = False
        for v in graph[u]:
            if capacity[u][v] > 0 and dist[v] > dist[u] + cost_graph[u][v]:
                dist[v] = dist[u] + cost_graph[u][v]
                predecessor[v] = u
                if not in_queue[v]:
                    dq.append(v)
                    in_queue[v] = True
    return dist[sink] != INF

def mcmf(source, sink):
    max_flow = 0
    min_cost = 0
    while spfa(source, sink) and dist[sink] < 0:
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

N = int(input())
items = []
for _ in range(N):
    x, y = map(int, input().split())
    items.append((x, y))

L_items = []
R_items = []
for (x, y) in items:
    if x < 0:
        L_items.append((x, y))
    elif x > 0:
        R_items.append((x, y))
        
base = 0.0
for (x, y) in L_items:
    base += -x
for (x, y) in R_items:
    base += x


L_count = len(L_items)
R_count = len(R_items)
total = L_count + R_count + 2
source = 0
sink = L_count + R_count + 1

graph = [[] for _ in range(total)]
capacity = [[0] * total for _ in range(total)]
cost_graph = [[0] * total for _ in range(total)]

# source -> L
for i in range(L_count):
    add_edge(source, 1 + i, 1, 0)
# R -> sink
for j in range(R_count):
    add_edge(1 + L_count + j, sink, 1, 0)

# L -> R
for i in range(L_count):
    x_i, y_i = L_items[i]
    for j in range(R_count):
        x_j, y_j = R_items[j]
        pairing_cost = math.sqrt((x_i + x_j)**2 + (y_i - y_j)**2)
        indiv_cost = (-x_i) + (x_j)
        extra_cost = pairing_cost - indiv_cost
        add_edge(1 + i, 1 + L_count + j, 1, extra_cost)

flow, cost = mcmf(source, sink)

ans = base + cost
print(f"{ans:.3f}")
