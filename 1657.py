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
    dist = [INF] * (n * m + 2)
    dist[source] = 0
    in_queue = [False] * (n * m + 2)
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

def get_number(y,x):
    return (y-1) * m + x

n, m = map(int, input().split())

graph = [[] for _ in range(n * m + 2)]
capacity = [[0] * (n * m + 2) for _ in range(n * m + 2)]
cost_graph = [[0] * (n * m + 2) for _ in range(n * m + 2)]
dist = [0] * (n * m + 2)
predecessor = [0] * (n * m + 2)

source = n * m
sink = n * m + 1

costs = [[10,8,7,5,1], [8,6,4,3,1], [7,4,3,2,1], [5,3,2,2,1], [1,1,1,1,0]]

li = []
for _ in range(n):
    s = list(map(str, input().rstrip()))
    for i in range(len(s)):
        if(s[i] == 'F'):
            s[i] = 'E'
    li.append(s)

for i in range(n):
    for j in range(m):
        if (i + j) & 1:
            add_edge(source, i * m + j, 1, 0)
            add_edge(i * m + j, sink, 1, 0)
            for k in range(4):
                nx = i + int("1012"[k]) - 1
                ny = j + int("2101"[k]) - 1
                if(nx < 0 or nx >= n or ny < 0 or ny >= m):
                    continue
                add_edge(i * m + j, nx * m + ny, 1, -costs[ord(li[i][j]) - ord('A')][ord(li[nx][ny]) - ord('A')])
        else:
            add_edge(i * m + j, sink, 1, 0)
            
max_flow, min_cost = mcmf(source, sink)
#print(max_flow)
print(min_cost * -1)