import sys
input = sys.stdin.readline
from collections import deque

def bfs(idx, i,j, visited,graph):
    q = deque()
    q.append((i,j,0))
    visited[i][j] = True
    dir = [(-1, -1), (1, 1), (1, -1), (-1, 1)]
    cnt = 0
    
    while q:
        x, y, t = q.popleft()
        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if graph[nx][ny] == 1 and not visited[nx][ny]:
                q.append((nx, ny, t+1))
                visited[nx][ny] = True
                
                for i in range(len(coord)):
                    if(nx == coord[i][0] and ny == coord[i][1]):
                            adj[idx][i] = t+1
                            adj[i][idx] = t+1
                            cnt += 1
                            
            if graph[nx][ny] == 0 and not visited[nx][ny]:
                q.append((nx, ny, t+1))
                visited[nx][ny] = True
                
def dfs(x, visited):
    if visited == (1 << count) - 1:     # 모든 도시를 방문했다면
        return 0  # 출발지로 되돌아오는 부분을 제거하고 0을 반환

    if dp[x][visited] != 10**10:       # 이미 최소비용이 계산되어 있다면
        return dp[x][visited]

    for i in range(1, count):           # 모든 도시를 탐방
        if not adj[x][i]:         # 가는 경로가 없다면 skip
            continue
        if visited & (1 << i):      # 이미 방문한 도시라면 skip
            continue

        # 점화식 부분(위 설명 참고)
        dp[x][visited] = min(dp[x][visited], dfs(i, visited | (1 << i)) + adj[x][i])
    return dp[x][visited]

n = int(input())
graph = []

for _ in range(n):
    li = list(map(int, input().split()))
    graph.append(li)

coord = []
count = 0
for i in range(n):
    for j in range(n):
        if(graph[i][j] == 1):
            coord.append((i,j))
            count += 1
        if(graph[i][j] == 2):
            coord.insert(0, (i,j))
            count += 1
            
adj = [[0] * count for _ in range(count)]

for i in range(len(coord)):
    visited = [[False] * n for _ in range(n)]
    bfs(i, coord[i][0], coord[i][1], visited, graph)

flag = True
for i in range(count):
    for j in range(count):
        if(i!=j and adj[i][j] == 0):
            flag = False
            break
        
if not (flag):
    print("Shorei")
else:
    print("Undertaker")
    dp = [[10**10] * (1 << count) for _ in range(count)]
    print(dfs(0, 1))