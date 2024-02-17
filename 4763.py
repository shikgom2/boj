import sys

input = sys.stdin.readline

def find(x):
    if x not in parent:
        parent[x] = x
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    if a != b:
        parent[b] = a


_len = float(input())
m = int(input())
for _ in range(m):
    name = input()

n = int(input())
edges = []
parent = {}
ans = 0

for i in range(n):
    lists = input().split()
    x,y = lists[0], lists[1]
    z = float(lists[2])
    edges.append((z, x, y))

edges.sort()

for edge in edges:
    z, x, y = edge
    if find(x) != find(y):
        union(x, y)
        ans += z
if(_len > ans):
    print(f'Need {ans:.1f} miles of cable')
else:
    print("Not enough cable")