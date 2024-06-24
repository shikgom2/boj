from collections import deque

def bfs(graph, source, sink, parent):
    visited = [False] * len(graph)
    queue = deque([source])
    visited[source] = True

    while queue:
        u = queue.popleft()

        for ind, val in enumerate(graph[u]):
            if not visited[ind] and val > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u

                if ind == sink:
                    return True

    return False

def edmonds_karp(graph, source, sink):
    parent = [-1] * len(graph)
    max_flow = 0

    while bfs(graph, source, sink, parent):
        path_flow = float("Inf")
        s = sink

        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]

        max_flow += path_flow

        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]

    return max_flow

n,m = map(int, input().split())
board = []
for _ in range(n):
    t = list(map(str, input().rstrip()))
    board.append(t)

graph = [[] for _ in range(2 * n * m)]

for i in range(n):
    for j in range(m):
        if(board[i][j] == '#'):
            continue
        elif(board[i][j] == 'K'):
            x, y = i,j
            start = m * i + j + m * n
        elif(board[i][j] == 'H'):
            z, w = i, j
            end = m * i + j
            continue

        graph[m * i + j].append(m * i + j + m * n)

        if i and (board[i - 1][j] not in 'K#'):
            graph[m * i + j + m * n].append(m * (i - 1) + j)
        
        if (i < n - 1) and (board[i + 1][j] not in 'K#'):
            graph[m * i + j + m * n].append(m * (i + 1) + j)
        
        if j and (board[i][j - 1] not in 'K#'):
            graph[m * i + j + m * n].append(m * i + j - 1)
        
        if (j < m - 1) and (board[i][j + 1] not in 'K#'):
            graph[m * i + j + m * n].append(m * i + j + 1)
        
if abs(x - z) + abs(y - w) == 1:
    print(-1)
    exit()

print(graph)
print(edmonds_karp(graph, start, end))