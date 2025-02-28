import sys
from collections import deque

input = sys.stdin.readline
INF = 10**9

def bfs(cap, source, sink, parent):

    visited = [False] * len(cap)
    queue = deque([source])
    visited[source] = True

    while queue:
        u = queue.popleft()
        for v in range(len(cap)):
            if not visited[v] and cap[u][v] > 0:
                visited[v] = True
                parent[v] = u
                if v == sink:
                    return True
                queue.append(v)
    return False

def edmonds_karp(cap, source, sink):

    parent = [-1]*len(cap)
    flow = 0

    while bfs(cap, source, sink, parent):
        path_flow = INF
        v = sink
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, cap[u][v])
            v = u
        flow += path_flow

        v = sink
        while v != source:
            u = parent[v]
            cap[u][v] -= path_flow
            cap[v][u] += path_flow
            v = u

    return flow

def i_in(i):
    return i
def i_out(i):
    return i+n

n, m = map(int, input().split())
orig_source, orig_sink = map(int, input().split())

cost = [0] + [int(input()) for _ in range(n)]

S = 0
T = 2*n + 1
size = 2*n + 2

cap = [[0]*size for _ in range(size)]

for i in range(1, n+1):
    cap[i_in(i)][i_out(i)] = cost[i]

for _ in range(m):
    u, v = map(int, input().split())
    cap[i_out(u)][i_in(v)] = INF
    cap[i_out(v)][i_in(u)] = INF

cap[S][i_in(orig_source)] = INF

cap[i_out(orig_sink)][T] = INF

max_flow = edmonds_karp(cap, S, T)

visited = [False]*size
queue = deque([S])
visited[S] = True
while queue:
    u = queue.popleft()
    for v in range(size):
        if not visited[v] and cap[u][v] > 0:
            visited[v] = True
            queue.append(v)

cut_vertices = []
for v in range(1, n+1):
    if visited[i_in(v)] and not visited[i_out(v)]:
        cut_vertices.append(v)

cut_vertices.sort()
print(*cut_vertices)
