import sys
input = sys.stdin.readline 
from collections import deque

def bfs(graph, source, sink, parent):
    visited = [False] * len(graph)
    queue = deque([source])
    visited[source] = True

    while queue:
        u = queue.popleft()

        for ind, val in enumerate(graph[u]):
            if not visited[ind] and val > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u

                if ind == sink:
                    return True

    return False

def edmonds_karp(graph, source, sink):
    parent = [-1] * len(graph)
    max_flow = 0

    while bfs(graph, source, sink, parent):
        path_flow = float("Inf")
        s = sink

        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]

        max_flow += path_flow

        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]

    return max_flow
    
while(True):
    n,m = map(int, input().split())
    if(n==0 and m == 0):
        break
    li = [0] + list(map(int, input().split()))
    graph = [[0] * (n+3) for _ in range(n+3)]

    source = 0
    sink = n+1

    for i in range(1, len(li)):
        if(li[i] == 1):
            graph[source][i] = 1
        else:
            graph[i][sink] = 1

    for _ in range(m):
        a,b = map(int ,input().split())
        graph[a][b] = 1
        graph[b][a] = 1
        '''
        if(li[a]== 1 and li[b] == 0):     
            graph[a][b] = 1
        elif(li[a] == 0 and li[b] == 1):
            graph[b][a] = 1
        else:
            graph[a][b] = 1
            graph[b][a] = 1
        '''
    print(edmonds_karp(graph, source, sink))