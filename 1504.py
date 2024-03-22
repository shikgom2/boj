import heapq

def dijkstra(graph, start, end):
    INF = int(1e9)
    distance = [INF] * (len(graph) + 1)
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        dist, node = heapq.heappop(queue)
        if distance[node] < dist:
            continue
        for next_node, next_dist in graph[node]:
            cost = dist + next_dist
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(queue, (cost, next_node))

    return distance[end]

V,E = map(int, input().split())
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))
    graph[end].append((start, cost))

v1, v2 = map(int, input().split())

res1 = dijkstra(graph, 1, v1)
res1 += dijkstra(graph, v1, v2)
res1 += dijkstra(graph, v2, V)

res2 = dijkstra(graph, 1, v2)
res2 += dijkstra(graph, v2, v1)
res2 += dijkstra(graph, v1, V)

res = min(res1, res2)
if(res >= 10**9):
    print(-1)
else:
    print(res)