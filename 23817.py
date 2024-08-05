import sys
input = sys.stdin.readline
from collections import deque

def bfs(start, x, y, graph, visited):
    q = deque()
    q.append((x, y, 0))
    visited[x][y] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    e = n
    v = m
    
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
            elif graph[nx][ny] != 'X' and not visited[nx][ny]:
                q.append((nx, ny, t + 1))
                visited[nx][ny] = True
    return

n, m = map(int, input().split())
graph = []
for _ in range(n):
    li = list(map(str, input().rstrip()))
    graph.append(li)

cnt = 1
graph_coord = [-1] * 21
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'S':
            graph[i][j] = 0
            graph_coord[0] = (i, j)
        elif graph[i][j] == 'K':
            graph[i][j] = cnt
            graph_coord[cnt] = (i, j)
            cnt += 1

adjust = [[-1] * cnt for _ in range(cnt)]

for i in range(cnt):
    visited = [[False] * m for _ in range(n)]
    bfs(i, graph_coord[i][0], graph_coord[i][1], graph, visited)

#find permulation n^5
    ans = 10**10
    for s1 in range(1, cnt):
        if adjust[0][s1] == -1:
            continue
        for s2 in range(1, cnt):
            if s2 == s1 or adjust[s1][s2] == -1:
                continue
            for s3 in range(1, cnt):
                if s3 == s1 or s3 == s2 or adjust[s2][s3] == -1:
                    continue
                for s4 in range(1, cnt):
                    if s4 == s1 or s4 == s2 or s4 == s3 or adjust[s3][s4] == -1:
                        continue
                    for s5 in range(1, cnt):
                        if s5 == s1 or s5 == s2 or s5 == s3 or s5 == s4 or adjust[s4][s5] == -1:
                            continue
                        ans = min(ans, adjust[0][s1] + adjust[s1][s2] + adjust[s2][s3] + adjust[s3][s4] + adjust[s4][s5])

if ans == 10**10:
    print(-1)
else:
    print(ans)
