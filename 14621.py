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
gender = list(map(str, input().split()))
edges = []
parent = [i for i in range(m + 1)]
ans = 0

for i in range(n):
    x, y, z = map(int, input().split())
    if(gender[x-1] != gender[y-1]):
        edges.append((z, x, y))

edges.sort()

cnt = 0
for edge in edges:
    z, x, y = edge
    if find(x) != find(y):
        union(x, y)
        ans = ans + z
        cnt += 1
 
if (cnt == m-1):
    print(ans)
else:
    print(-1)