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

for i in range(n+1):
    x, y, z = map(int, input().split())
    edges.append((not z, x, y))

edges.sort(key=lambda x:x[0])
for edge in edges:
    z, x, y = edge
    if find(x) != find(y):
        union(x, y)
        ans += z
        
worst_ans = ans

ans = 0
edges.sort(reverse=True, key=lambda x:x[0])
parent = [i for i in range(m + 1)]

for edge in edges:
    z, x, y = edge
    if find(x) != find(y):
        union(x, y)
        ans += z

best_ans = ans

print(abs((worst_ans**2) - (best_ans**2)))