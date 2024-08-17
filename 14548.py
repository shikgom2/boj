import sys
input = sys.stdin.readline
import heapq

def dijkstra(graph, start, end):
    INF = int(1e9)
    dist = [INF] * (len(graph) + 1)
    dist[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        current_dist, node = heapq.heappop(pq)
        
        if dist[node] < current_dist:
            continue
        
        for v, w in graph[node]:
            cost = current_dist + w
            if cost < dist[v]:
                dist[v] = cost
                heapq.heappush(pq, (cost, v))

    return dist[end]

t = int(input())
for _ in range(t):
    n, w1, w2 = input().rstrip().split()
    n = int(n)
    graph = [[] for _ in range(int(n) + 1)]
    
    dir = {}
    world = 0
    for i in range(n):
        s1, s2, k = input().rstrip().split()

        if(s1 not in dir):
            world += 1
            dir[s1] = world
        if(s2 not in dir):
            world += 1
            dir[s2] = world

        start = dir[s1]
        end = dir[s2]
        graph[int(start)].append((int(end), int(k)))
        graph[int(end)].append((int(start), int(k)))
    
    start = dir[w1]
    end = dir[w2]

    print(f"{w1} {w2} {dijkstra(graph, int(start), int(end))}")
