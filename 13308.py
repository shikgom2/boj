import sys
input = sys.stdin.readline
import heapq

def dijkstra():
    INF = int(1e11)
    distance = [[INF] * (max(li) + 1) for _ in range(n + 1)]
    q = []
    distance[1][li[1]] = 0
    heapq.heappush(q, (0, li[1], 1))
    while q:
        now_dist, now_cost, now = heapq.heappop(q)
        if now == n:
            return now_dist
        if distance[now][now_cost] < now_dist:
            continue
        for (next, next_dist) in graph[now]:
            next_cost = min(li[next], now_cost)
            if distance[next][now_cost] > now_dist + now_cost * next_dist:
                distance[next][now_cost] = now_dist + now_cost * next_dist
                heapq.heappush(q, (now_dist + now_cost * next_dist, next_cost, next))

n,m = map(int, input().split())
li = [-1] + list(map(int, input().split()))

dp = [[] for _ in range(n+1)]
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))
    graph[end].append((start, cost))

print(dijkstra())