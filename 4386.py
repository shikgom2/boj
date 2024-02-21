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

x_list = []
y_list = []

for i in range(n):
    x, y= map(float, input().split())
    x_list.append(x)
    y_list.append(y)
    #edges.append((z, x, y))

for i in range(n):
    for j in range(i+1, n):
        x1 = x_list[i]
        y1 = y_list[i]
        x2 = x_list[j]
        y2 = y_list[j]
        dist = ((x1-x2)**2 + (y1-y2)**2)**(1/2)

        edges.append((dist, i, j))

edges.sort()

for edge in edges:
    z, x, y = edge
    if find(x) != find(y):
        union(x, y)
        ans = ans + z
print(f"{ans:.2f}")