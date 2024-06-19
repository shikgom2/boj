import heapq

def dijkstra(graph, start, end):
    INF = int(1e11)
    distance = [INF] * (len(graph) + 1)
    prev_node = [-1] * (len(graph) + 1)  # 이전 노드를 저장할 배열
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

    # 최소 경로 추적
    path = []
    current = end
    while current != -1:
        path.append(current)
        current = prev_node[current]
    path = path[::-1]
    
    return distance[end], path

n,m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))
    
i,j,k = map(int, input().split())

ans1 = dijkstra(graph, i, j)[0]
ans2 = dijkstra(graph, j, k)[0]

ans1 += ans2
if(ans1 > 10 ** 10):
    print(-1, end=" ")
else:
    print(ans1, end=" ")

       
graph[j] = ""

ans2 = dijkstra(graph, i, k)
if(ans2[0] > 10 ** 10):
    print(-1)
else:
    print(ans2[0])