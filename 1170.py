import sys
input = sys.stdin.readline


def check(node, graph, visited, parent, low, disc, time):
    stack = [(node, iter(graph[node]))]
    visited[node] = True
    low[node] = disc[node] = time[0]
    time[0] += 1

    while stack:
        u, neighbors = stack[-1]
        for v in neighbors:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                low[v] = disc[v] = time[0]
                time[0] += 1
                stack.append((v, iter(graph[v])))
                break
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])
        else:
            if len(stack) > 1:
                v, _ = stack.pop()
                u, _ = stack[-1]
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    return False
            else:
                stack.pop()

    for i in range(len(graph)):
        if parent[i] != -1 and low[i] > disc[parent[i]]:
            return False

    return True

def cactus(graph):
    visited = [False] * len(graph)
    parent = [-1] * len(graph)
    low = [float('inf')] * len(graph)
    disc = [float('inf')] * len(graph)
    time = [0]
    ans = 0

    for i in range(len(graph)):
        if not visited[i]:
            if check(i, graph, visited, parent, low, disc, time):
                ans += 1

    return ans

n,m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    u,v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

print(cactus(graph))