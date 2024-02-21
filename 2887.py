import sys

input = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    parent[max(a, b)] = min(a, b)

m = int(input())

temp_edges = []
edges = []
parent = [i for i in range(m + 1)]
ans = 0

for i in range(m):
    x, y, z = map(int, input().split())
    temp_edges.append((x, y, z, i))

for i in range(3):
    temp_edges.sort(key=lambda x:x[i])
    for j in range(1, m):
        edges.append((abs(temp_edges[j-1][i]-temp_edges[j][i]),temp_edges[j-1][3],temp_edges[j][3]))
edges.sort()

for edge in edges:
    z, x, y = edge
    if find(x) != find(y):
        union(x, y)
        ans = ans + z
print(ans)