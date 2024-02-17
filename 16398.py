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

n = int(input())

edges = []
parent = [i for i in range(n + 1)]
ans = 0

for i in range(n):
    weights = list(map(int, input().split()))
    
    for j in range(len(weights)):
        edges.append((weights[j], i, j))

edges.sort()

for edge in edges:
    z, x, y = edge
    if find(x) != find(y):
        union(x, y)
        ans += z
print(ans)