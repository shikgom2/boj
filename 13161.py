import sys
from collections import deque
input = sys.stdin.readline

INF = 10**9

def add_edge(u, v, cap):
    graph[u].append([v, cap, len(graph[v])])
    graph[v].append([u, 0, len(graph[u]) - 1])

def bfs():
    level = [-1] * N_total
    level[S] = 0
    q = deque([S])
    while q:
        u = q.popleft()
        for v, cap, _ in graph[u]:
            if cap and level[v] < 0:
                level[v] = level[u] + 1
                q.append(v)
    return level

def dfs_flow(u, f, level, it):
    if u == T:
        return f
    while it[u] < len(graph[u]):
        v, cap, rev = graph[u][it[u]]
        if cap and level[u] + 1 == level[v]:
            pushed = dfs_flow(v, min(f, cap), level, it)
            if pushed:
                graph[u][it[u]][1] -= pushed
                graph[v][rev][1] += pushed
                return pushed
        it[u] += 1
    return 0

n = int(input().strip())
li = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(n)]

liA = [i for i, v in enumerate(li) if v == 1]
liB = [i for i, v in enumerate(li) if v == 2]

if (not liA) or (not liB):
    if not liA and not liB:
        groupA = list(range(1, n+1))
        groupB = []
    elif liA and not liB:
        groupA = list(range(1, n+1))
        groupB = []
    else:
        groupA = []
        groupB = list(range(1, n+1))
    print(0)
    print(" ".join(map(str, sorted(groupA))))
    print(" ".join(map(str, sorted(groupB))))
    exit()

N_total = n + 2
S = n
T = n + 1
graph = [[] for _ in range(N_total)]

for i in liA:
    add_edge(S, i, INF)
for i in liB:
    add_edge(i, T, INF)

for i in range(n):
    for j in range(i+1, n):
        w = arr[i][j]
        if w > 0:
            add_edge(i, j, w)
            add_edge(j, i, w)

max_flow = 0
while True:
    level = bfs()
    if level[T] < 0:
        break
    it = [0] * N_total
    while True:
        pushed = dfs_flow(S, INF, level, it)
        if not pushed:
            break
        max_flow += pushed
        
visited = [False] * N_total
dq = deque([S])
while dq:
    u = dq.popleft()
    if visited[u]:
        continue
    visited[u] = True
    for v, cap, _ in graph[u]:
        if cap and not visited[v]:
            dq.append(v)

groupA = []
groupB = []
for i in range(n):
    if visited[i]:
        groupA.append(i+1)
    else:
        groupB.append(i+1)

groupA.sort()
groupB.sort()
print(max_flow)
print(" ".join(map(str, groupA)))
print(" ".join(map(str, groupB)))
