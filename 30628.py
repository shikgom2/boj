import sys
input = sys.stdin.readline 
import heapq

def dijkstra(graph, start, end, k):
    INF = int(1e10)
    n = len(graph)
    
    # dp[i][j]: i th node to go exactly j weight
    dp = [[INF] * (k + 1) for _ in range(n + 1)]
    dp[start][0] = 0
    pq = []
    heapq.heappush(pq, (0, start, 0))
    
    while pq:
        current_cost, node, current_distance = heapq.heappop(pq)
        if current_distance > k:
            continue
        if node == end and current_distance == k:
            return True
        if current_cost > dp[node][current_distance]:
            continue
        for neighbor, weight in graph[node]:
            next_distance = current_distance + weight
            next_cost = current_cost + weight
        
            if next_distance <= k and next_cost < dp[neighbor][next_distance]:
                dp[neighbor][next_distance] = next_cost
                heapq.heappush(pq, (next_cost, neighbor, next_distance))
    
    return dp[end][k] != INF
n,m,k = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    i,j,w = map(int ,input().split())
    graph[i].append((j,w))
    graph[j].append((i,w))

if(dijkstra(graph,1,n,k)):
    print("YES")
else:
    print("NO")