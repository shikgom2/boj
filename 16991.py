import sys
input = sys.stdin.readline
import math

def dist(x1, y1, x2, y2):
    dist= math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return dist

def dfs(x, visited):
    if visited == (1 << n) - 1:     # 모든 도시를 방문했다면
        if graph[x][0]:             # 출발점으로 가는 경로가 있을 때
            return graph[x][0]
        else:                       # 출발점으로 가는 경로가 없을 때
            return 10**10

    if dp[x][visited] != 10**10:       # 이미 최소비용이 계산되어 있다면
        return dp[x][visited]

    for i in range(1, n):           # 모든 도시를 탐방
        if not graph[x][i]:         # 가는 경로가 없다면 skip
            continue
        if visited & (1 << i):      # 이미 방문한 도시라면 skip
            continue

        # 점화식 부분(위 설명 참고)
        dp[x][visited] = min(dp[x][visited], dfs(i, visited | (1 << i)) + graph[x][i])
    return dp[x][visited]

n = int(input())
graph = [[0] * n for _ in range(n)]
li = []
for _ in range(n):
    a,b = map(int, input().split())
    li.append((a,b))

for i in range(n):
    for j in range(n):
        graph[i][j] = dist(li[i][0], li[i][1], li[j][0], li[j][1])
        
dp = {}
print(dfs(0, 1))