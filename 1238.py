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

m, n, s = map(int, input().split())
edges = []
dist = [0] * (m+1)

for i in range(n):
    x, y, z = map(int, input().split())
    edges.append((z, x, y))

for i in range(1, (m+1)):
    distances = dijkstra(edges, i)

    for j in range(1, len(distances)):
        d = distances[j]
        #print(f"{i} -> {j} : {d}")

        if(s == j):
           dist[i] = d

distances = dijkstra(edges, s)
for i in range(1, len(distances)):
    dist[i] += distances[i]

print(max(dist))