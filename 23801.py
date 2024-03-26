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
    
    return distance[end]

V,E = map(int, input().split())
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))
    graph[end].append((start, cost))
    
x, z = map(int, input().split())

i=int(input())
li = list(map(int, input().split()))

res = 10**11
for i in li:
    val = dijkstra(graph, x, i) + dijkstra(graph, i, z)
    res = min(res, val)

if(res >= 10**11):
    print(-1)
else:
    print(res)
