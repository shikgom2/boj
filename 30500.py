import sys
input = sys.stdin.readline
from collections import defaultdict

def dfs(u):
    stack = [(u, False)]
    while stack:
        node, processed = stack.pop()
        if processed:
            order.append(node)
        else:
            if visited[node]:
                continue
            visited[node] = True
            stack.append((node, True))
            for v in graph[node]:
                if not visited[v]:
                    stack.append((v, False))

def reverse_dfs(u, current_scc):
    stack = [u]
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            scc_id[node] = current_scc
            for v in reverse_graph[node]:
                if not visited[v]:
                    stack.append(v)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
reverse_graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    reverse_graph[b].append(a)

visited = [False] * (n + 1)
order = []

for u in range(1, n + 1):
    if not visited[u]:
        dfs(u)

scc_id = [0] * (n + 1)
current_scc = 0
visited = [False] * (n + 1)

for u in reversed(order):
    if not visited[u]:
        current_scc += 1
        reverse_dfs(u, current_scc)

in_degree = [0] * (current_scc + 1)
dic = defaultdict(set)
for u in range(1, n + 1):
    for v in graph[u]:
        if scc_id[u] != scc_id[v]:
            if scc_id[v] not in dic[scc_id[u]]:
                dic[scc_id[u]].add(scc_id[v])
                in_degree[scc_id[v]] += 1

ans = 0
for i in range(1, current_scc + 1):
    if in_degree[i] == 0:
        ans += 1

print(ans)