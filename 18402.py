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

edges = []


V = int(input())
exit = int(input())
time = int(input())
E = int(input())

graph = [[] for _ in range(E + 1)]

for _ in range(E):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

cnt = 0
for i in range(1, V+1):
    res = dijkstra(graph, i, exit)
    if(res <= time):
        cnt+=1
print(cnt)