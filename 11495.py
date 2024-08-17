import sys
from collections import deque

INF = float('inf')

def add_edge(u, v, cap):
    graph[u].append(v)
    graph[v].append(u)
    capacity[u][v] = cap
    capacity[v][u] = 0  # 역방향 간선의 용량은 0으로 초기화

def bfs(source, sink):
    global predecessor
    predecessor = [-1] * (n * m + 2)
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

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    maps = []

    s = 0
    for _ in range(n):
        l = list(map(int, input().split()))
        maps.append(l)
        s += sum(l)

    graph = [[] for _ in range(n * m + 2)]
    capacity = [[0] * (n * m + 2) for _ in range(n * m + 2)]

    source = 0
    sink = n * m + 1

    for i in range(n):
        for j in range(m):
            if (i + j) % 2:
                add_edge(i * m + j + 1, sink, maps[i][j])
            else:
                add_edge(source, i * m + j + 1, maps[i][j])
                dx = [0, 0, 1, -1]
                dy = [1, -1, 0, 0]
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if 0 <= nx < n and 0 <= ny < m:
                        add_edge(i * m + j + 1, nx * m + ny + 1, INF)

    max_flow = edmonds_karp(source, sink)
    print(s - max_flow)
