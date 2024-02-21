import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def find_scc_dfs(index):
    visited[index] = True
    for next_index in graph[index]:
        if not visited[next_index]:
            find_scc_dfs(next_index)
    stack.append(index)

def build_scc(index):
    visited[index] = True
    ids[index] = scc_count
    scc_members.append(index)
    for next_index in reverse_graph[index]:
        if not visited[next_index]:
            build_scc(next_index)

for _ in range(int(input())):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    reverse_graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        x, y = map(int, input().split())
        graph[x].append(y)
        reverse_graph[y].append(x)

    stack = []
    visited = [False] * (N + 1)
    for node in range(1, N + 1):
        if not visited[node]:
            find_scc_dfs(node)

    visited = [False] * (N + 1)
    ids = [-1] * (N + 1)
    scc_count = 0
    while stack:
        node = stack.pop()
        if not visited[node]:
            scc_members = []
            build_scc(node)
            scc_count += 1

    print(scc_members)
    
    in_degree = [0] * scc_count
    for node in range(1, N + 1):
        for next_node in graph[node]:
            if ids[node] != ids[next_node]:
                in_degree[ids[next_node]] += 1

    answer = sum(1 for count in in_degree if count == 0)
    print(answer)