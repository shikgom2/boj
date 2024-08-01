import sys
input = sys.stdin.readline
import heapq
#TLE about floyd-warshall (n^3)

def dijkstra(graph, start, end):
    INF = int(1e9)
    dist = [INF] * (len(graph) + 1)
    dist[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        dist, node = heapq.heappop(pq)
        if dist[node] < dist:
            continue
        for v, w in graph[node]:
            cost = dist + w
            if cost < dist[v]:
                dist[v] = cost
                heapq.heappush(pq, (cost, v))

    return dist[end]

n,m = map(int, input().split())
graph = {i : [] for i in range(n)}

for _ in range(m):
    a,b,t = map(int, input().split())
    graph[a].append((b, t))
    graph[b].append((a, t))

dist = dijkstra(graph, 0, n-1)
dist2 = dijkstra(graph, n-1, 0)

ans = 0
for u in range(n):
    for v,w in graph[u]:
        if(dist[u] + w + dist2[v] == dist[n-1]):
            ans += w
print(ans * 2)