import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(u, p, adj, visited, parent):
    global found_cycle, cycle_nodes
    if found_cycle:
        return
    visited[u] = 1
    for v, w in adj[u]:
        if v == p:
            continue
        if visited[v] == 0:
            parent[v] = u
            dfs(v, u, adj, visited, parent)
            if found_cycle:
                return
        elif visited[v] == 1:
            if not found_cycle:
                found_cycle = True
                curr = u
                cycle_nodes = [curr]
                while curr != v:
                    curr = parent[curr]
                    cycle_nodes.append(curr)
                cycle_nodes.reverse()
                return
    visited[u] = 2

def dfs2(u, p, adj, anc, dist_to_anc):
    for v, w in adj[u]:
        if v != p and anc[v] == -1:
            anc[v] = anc[u]
            dist_to_anc[v] = dist_to_anc[u] + w
            dfs2(v, u, adj, anc, dist_to_anc)

while True:
    n = int(input())
    if n == 0:
        break
    adj = [[] for _ in range(n)]
    
    for _ in range(n):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))

    visited = [0] * n
    parent = [-1] * n
    global cycle_nodes, found_cycle
    cycle_nodes = []
    found_cycle = False

    dfs(0, -1, adj, visited, parent)

    K = len(cycle_nodes)
    cycle_edges = []
    for i in range(K):
        u1 = cycle_nodes[i]
        u2 = cycle_nodes[(i + 1) % K]
        for vv, ww in adj[u1]:
            if vv == u2:
                cycle_edges.append(ww)
                break

    cum_dist = [0] * (K + 1)
    for i in range(K):
        cum_dist[i + 1] = cum_dist[i] + cycle_edges[i]
    L = cum_dist[K]

    pos_in_cycle = [-1] * n
    for idx, node in enumerate(cycle_nodes):
        pos_in_cycle[node] = idx

    anc = [-1] * n
    dist = [0] * n

    for node in cycle_nodes:
        anc[node] = node
        dist[node] = 0

    for node in cycle_nodes:
        dfs2(node, -1, adj, anc, dist)

    q = int(input())
    for _ in range(q):
        u, v = map(int, input().split())
        du = dist[u]
        dv = dist[v]
        au = anc[u]
        av = anc[v]
        if au == av:
            cycle = 0
        else:
            idx_u = pos_in_cycle[au]
            idx_v = pos_in_cycle[av]
            d1 = abs(cum_dist[idx_u] - cum_dist[idx_v])
            d2 = L - d1
            cycle = min(d1, d2)
        ans = du + dv + cycle
        print(int(ans))