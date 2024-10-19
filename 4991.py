import sys
input = sys.stdin.readline
from collections import deque

def bfs(start, x, y, graph, visited):
    q = deque()
    q.append((x, y, 0))
    visited[x][y] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    e = m
    v = n
    
    count = 0
    while q:
        x, y, t = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= e or ny < 0 or ny >= v:
                continue

            if start != graph[nx][ny] and isinstance(graph[nx][ny], int) and not visited[nx][ny]:  #is int => graph's vertex
                #print(f"{start} -> {graph[nx][ny]} : {t+1}")
                adjust[start][graph[nx][ny]] = t + 1
                q.append((nx, ny, t + 1))
                count += 1
                visited[nx][ny] = True
                if count == cnt - 1: # if all found, early return 
                    return
            elif graph[nx][ny] != 'x' and not visited[nx][ny]:
                q.append((nx, ny, t + 1))
                visited[nx][ny] = True
    return

while(True):
    n, m = map(int, input().split())
    if(n == 0 and m == 0):
        break
    
    graph = []
    for _ in range(m):
        li = list(map(str, input().rstrip()))
        graph.append(li)

    cnt = 1
    graph_coord = [-1] * 21
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 'o':
                graph[i][j] = 0
                graph_coord[0] = (i, j)
            elif graph[i][j] == '*':
                graph[i][j] = cnt
                graph_coord[cnt] = (i, j)
                cnt += 1

    adjust = [[-1] * cnt for _ in range(cnt)]
    
    for i in range(cnt):
        visited = [[False] * n for _ in range(m)]
        bfs(i, graph_coord[i][0], graph_coord[i][1], graph, visited)
    
    '''
    for i in range(cnt):
        print(adjust[i])
    '''
    
    INF = float('inf')
    n = len(adjust)

    dp = [[INF] * n for _ in range(1 << n)]
    dp[1][0] = 0

    for mask in range(1 << n):
        for u in range(n):
            if dp[mask][u] == INF:
                continue
            for v in range(n):
                if adjust[u][v] != -1 and not (mask & (1 << v)):
                    next_mask = mask | (1 << v)
                    dp[next_mask][v] = min(dp[next_mask][v], dp[mask][u] + adjust[u][v])

    final_mask = (1 << n) - 1
    ans = 10**10

    for i in range(1, n):
        ans = min(ans, dp[final_mask][i])

    if ans == 10**10:
        print(-1)
    else:
        print(ans)