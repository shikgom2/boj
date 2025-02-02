import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
edges = []
flow_values = set()
for _ in range(M):
    a, b, cost, flow = map(int, input().split())
    edges.append((a, b, cost, flow))
    flow_values.add(flow)

best_ratio = 0.0
for candidate_flow in flow_values:
    graph = {i: [] for i in range(1, N+1)}
    for a, b, cost, flow in edges:
        if flow >= candidate_flow:
            graph[a].append((b, cost))
            graph[b].append((a, cost))
    
    dist = {i: float('inf') for i in range(1, N+1)}
    dist[1] = 0
    heap = [(0, 1)]
    while heap:
        current_cost, node = heapq.heappop(heap)
        if current_cost != dist[node]:
            continue
        if node == N:
            break
        for neighbor, edge_cost in graph[node]:
            new_cost = current_cost + edge_cost
            if new_cost < dist[neighbor]:
                dist[neighbor] = new_cost
                heapq.heappush(heap, (new_cost, neighbor))
    
    if dist[N] != float('inf'):
        ratio = candidate_flow / dist[N]
        if ratio > best_ratio:
            best_ratio = ratio
            
print(int(best_ratio * 1000000))
    