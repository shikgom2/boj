import heapq

def dijkstra(graph, start, end):
    INF = int(1e11)
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
li = list(map(int, input().split()))

graph = [[] for _ in range(V+1)]

for _ in range(E):
    start, end, cost = map(int, input().split())
    if(start == V-1 or end == V-1):
        graph[start+1].append((end+1, cost))
        graph[end+1].append((start+1, cost))
    elif(li[start] == 1 or li[end] == 1):
        continue
    else:
        graph[start+1].append((end+1, cost))
        graph[end+1].append((start+1, cost))

res = dijkstra(graph, 1, V)
if(res >= 10**11):
    print(-1)
else:
    print(res)