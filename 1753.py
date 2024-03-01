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

m, n = map(int, input().split())
s = int(input())

edges = []

for i in range(n):
    x, y, z = map(int, input().split())
    edges.append((z, x, y))
distances = dijkstra(edges, s)

for i in range(1, len(distances)):
    s = str(distances[i])
    print(s.upper())