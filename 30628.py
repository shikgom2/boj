import sys
input = sys.stdin.readline 
import heapq

def dijkstra(graph, start, end, k):
    INF = int(1e10)
    n = len(graph)
    MOD = 12

    # dp[i][j]: minimum cost to reach node i with time j % MOD
    dp = [[INF] * MOD for _ in range(n)]
    dp[start][0] = 0
    pq = []
    heapq.heappush(pq, (0, start, 0))

    while pq:
        current_cost, node, current_time_mod = heapq.heappop(pq)
        
        if current_cost > dp[node][current_time_mod]:
            continue

        for neighbor, weight in graph[node]:
            next_time_mod = (current_time_mod + weight) % MOD
            next_cost = current_cost + weight

            if next_cost < dp[neighbor][next_time_mod]:
                dp[neighbor][next_time_mod] = next_cost
                heapq.heappush(pq, (next_cost, neighbor, next_time_mod))

    for i in range(k // MOD + 1):
        if dp[end][k % MOD] <= k:
            return True

    return False

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