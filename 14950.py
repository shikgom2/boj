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

n,m,t = map(int, input().split())

edges = []
parent = [i for i in range(n + 1)]

for i in range(m):
    x, y, z = map(int, input().split())
    edges.append((x,y,z))

edges.sort(key=lambda x:x[2])

ans = 0
cnt = 0
for edge in edges:
    x,y,z = edge
    if find(x) != find(y):
        union(x, y)
        ans = ans + z + (t * cnt)
        cnt += 1
print(ans)