import sys
input = sys.stdin.readline
import heapq

def dijkstra(pq, dist, adj):
    while pq:
        tot_cost, current = heapq.heappop(pq)
        if tot_cost > dist[current]:
            continue
        for neighbor, weight in adj[current]:
            next_cost = tot_cost + weight
            if next_cost < dist[neighbor]:
                dist[neighbor] = next_cost
                heapq.heappush(pq, (next_cost, neighbor))

v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]
 
for _ in range(e):
    a,b,c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

m, x = map(int, input().split())
dist1 = [10**10] * (v + 1)
pq = []

mac_li = list(map(int, input().split()))
for i in range(len(mac_li)):
    dist1[mac_li[i]] = 0
    heapq.heappush(pq, (0, mac_li[i]))

dijkstra(pq, dist1, graph)

s, y = map(int, input().split())
dist2 = [10**10] * (v + 1)
pq = []

star_li = list(map(int, input().split()))
for i in range(len(star_li)):
    dist2[star_li[i]] = 0
    heapq.heappush(pq, (0, star_li[i]))

dijkstra(pq, dist2, graph)

dis = 10**10
for i in range(1, v + 1):
    if dist1[i] != 0 and dist2[i] != 0 and dist1[i] <= x and dist2[i] <= y:
        total_dist = dist1[i] + dist2[i]
        if total_dist < dis:
            dis = total_dist

print(dis if dis != 10**10 else -1)
