import sys
input = sys.stdin.readline

def init_union_find(size):
    return [i for i in range(size)]

def find(root, x):
    if root[x] == x:
        return x
    root[x] = find(root, root[x])
    return root[x]

def union(root, x, y):
    rootX = find(root, x)
    rootY = find(root, y)
    if rootX != rootY:
        root[rootY] = rootX

def connected(root, x, y):
    return find(root, x) == find(root, y)

def kruskal(nodes, edges):
    mst = []
    cost = 0
    root = init_union_find(len(nodes))

    edges = sorted(edges, key=lambda x: x[2], reverse=False)

    for edge in edges:
        v, e, w = edge
        if not connected(root, v, e):
            union(root, v, e)
            mst.append(edge)
            cost += w

    #print(mst)
    return cost

while(True):
    graph_edges = []
    N,M = map(int, input().split())
    if(N== 0 and M==0):
        break
    sum = 0
    for _ in range(M):
        v,e,w = map(int, input().split())
        graph_edges.append((v,e,w))
        sum = sum + w

    mst_cost = kruskal(list(range(N + 1)), graph_edges)  
    print(sum - mst_cost)