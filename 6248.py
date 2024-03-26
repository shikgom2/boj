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

V,E,X = map(int, input().split())
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))
    graph[end].append((start, cost))


res = 0
for i in range(1, V+1):
    res = max(res, dijkstra(graph, X, i) + dijkstra(graph, i, X))

print(res)