import sys
input = sys.stdin.readline

def dfs(node, graph, visited, parent):
    visited[node] = True
    stack = [(node, -1)]  # (current_node, parent_node)
    cycles = 0

    while stack:
        u, p = stack.pop()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                stack.append((v, u))
            elif v != p:
                cycles += 1
                if cycles > 1:
                    return False
    return True

def cactus(graph):
    visited = [False] * len(graph)
    
    for i in range(len(graph)):
        if not visited[i]:
            if not dfs(i, graph, visited, -1):
                print("Not cactus")
                exit()
    print("Cactus")
    exit()
    
n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

cactus(graph)