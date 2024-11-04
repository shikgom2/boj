import sys
import heapq
input = sys.stdin.readline

def solve(N, K, graph):
    INF = float('inf')
    dp = [[INF] * (1 << N) for _ in range(N)]
    dp[K][1 << K] = 0
    
    queue = []
    heapq.heappush(queue, (0, K, 1 << K))  # (현재 비용, 현재 행성, 방문 상태)

    while queue:
        cost, current, visited = heapq.heappop(queue)

        if dp[current][visited] < cost:
            continue

        for next in range(N):
            next_visited = visited | (1 << next)
            next_cost = cost + graph[current][next]

            if dp[next][next_visited] > next_cost:
                dp[next][next_visited] = next_cost
                heapq.heappush(queue, (next_cost, next, next_visited))

    # 모든 행성을 방문한 상태에서의 최소 비용 찾기
    full_visited = (1 << N) - 1
    ans = min(dp[i][full_visited] for i in range(N))

    return ans

N, K = map(int, input().split())
graph = []
for _ in range(N):
    li = list(map(int, input().split()))
    graph.append(li)
    
ans = solve(N, K, graph)
print(ans)
