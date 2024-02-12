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

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

start_city, end_city = map(int, input().split())

result = dijkstra(graph, start_city, end_city)

print(result)