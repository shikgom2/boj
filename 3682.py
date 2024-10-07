import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(graph, v, visited, stack):
    visited[v] = True
    for w in graph[v]:
        if not visited[w]:
            dfs(graph, w, visited, stack)
    stack.append(v)

def reverseDFS(graph, v, visited, component, scc_id, node_to_scc):
    visited[v] = True
    component.append(v)
    node_to_scc[v] = scc_id
    for w in graph[v]:
        if not visited[w]:
            reverseDFS(graph, w, visited, component, scc_id, node_to_scc)

t = int(input())
for _ in range(t):
    V, E = map(int, input().split())

    graph = [[] for _ in range(V + 1)]
    reverse_graph = [[] for _ in range(V + 1)]
    for i in range(E):
        a,b = map(int, input().split())
        graph[a].append(b)
        reverse_graph[b].append(a)

    visited = [False] * (V + 1)
    stack = []

    for i in range(1, V + 1):
        if not visited[i]:
            dfs(graph, i, visited, stack)

    visited = [False] * (V + 1)
    results = []
    node_to_scc = {}
    scc_id = 0
    while stack:
        node = stack.pop()
        if not visited[node]:
            component = []
            reverseDFS(reverse_graph, node, visited, component, scc_id, node_to_scc)
            results.append(sorted(component))
            scc_id += 1

    #scc to node
    condensed_graph = [[] for _ in range(scc_id)]
    indegree = [0] * scc_id
    outdegree = [0] * scc_id 
    edge_set = set()

    for u in range(1, V + 1):
        for v in graph[u]:
            scc_u = node_to_scc[u]
            scc_v = node_to_scc[v]
            if scc_u != scc_v:
                if (scc_u, scc_v) not in edge_set:
                    condensed_graph[scc_u].append(scc_v)
                    edge_set.add((scc_u, scc_v))
                    outdegree[scc_u] += 1
                    indegree[scc_v] += 1

    in_cnt = 0
    out_cnt = 0
    for i in range(scc_id):
        if not indegree[i]:
            in_cnt += 1
        if not (outdegree[i]):
            out_cnt += 1
    if scc_id == 1:
        print(0)
        continue
            
    print(max(in_cnt, out_cnt))