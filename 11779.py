import heapq

def dijkstra(graph, start, end):
    INF = int(1e11)
    distance = [INF] * (len(graph) + 1)
    prev_node = [-1] * (len(graph) + 1)
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
                prev_node[next_node] = node
                heapq.heappush(queue, (cost, next_node))

    path = []
    current = end
    while current != -1:
        path.append(current)
        current = prev_node[current]
    path = path[::-1]
    
    return distance[end], path

V = int(input())
E = int(input())
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

ts, te = map(int, input().split())

res = dijkstra(graph, ts, te)
print(res[0])
print(len(res[1]))
print(*res[1])