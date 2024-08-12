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
parent = [i for i in range(311)]

for i in range(n):
    k = int(input())
    edges.append((0, i+1, k))

for i in range(n):
    li = list(map(int, input().split()))
    for j in range(n):
        if(i == j):
            continue
        else:
            edges.append((i+1, j+1, li[j]))

edges.sort(key=lambda x:x[2])

ans = 0
for edge in edges:
    x,y,z = edge
    if find(x) != find(y):
        union(x, y)
        ans = ans + z
print(ans)

