import heapq

def init(edges):
    graph = {}
    for z, x, y in edges:
        if x not in graph:
            graph[x] = []
        graph[x].append((y, z))
    return graph

def dijkstra(edges, start):
    graph = init(edges)
    max_node = max(max(x, y) for _, x, y in edges)
    dist = [float('INF')] * (max_node + 1)
    dist[start] = 0
    pq = [(0, start)]
    
    while pq:
        d, v = heapq.heappop(pq)
        if dist[v] < d:
            continue
        for n, w in graph.get(v, []):
            di = d + w
            if di < dist[n]:
                dist[n] = di
                heapq.heappush(pq, (di, n))
    return dist

m = int(input())
n = int(input())

edges = []

for i in range(n):
    x, y, z = map(int, input().split())
    edges.append((z, x, y))

for s in range(1, m+1):
    distances = dijkstra(edges, s)

    for i in range(1, len(distances)):
        s = str(distances[i])
        if(s == 'inf'):
            s = 0
        print(s, end=" ")
    print("")