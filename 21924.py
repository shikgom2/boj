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

m, n = map(int, input().split())

edges = []
parent = [i for i in range(m + 1)]
ans = 0

for i in range(n):
    x, y, z = map(int, input().split())
    edges.append((z, x, y))

edges.sort()

for edge in edges:
    z, x, y = edge
    if find(x) != find(y):
        union(x, y)
    else:
        ans += z

connected = True
root = find(1)
for i in range(2, m + 1):
    if find(i) != root:
        connected = False
        break

if(connected):
    print(ans)
else:
    print(-1)