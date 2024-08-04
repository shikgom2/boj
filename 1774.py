import sys
input = sys.stdin.readline 
import math

def dist(x1, y1, x2, y2):
    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return d

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    parent[max(a, b)] = min(a, b)

n,m = map(int, input().split())
parent = [i for i in range(n + 1)]

li = []
for _ in range(n):
    x,y = map(int, input().split())
    li.append((x,y))

already = []
for _ in range(m):
    s, e = map(int, input().split())
    already.append((s,e))

graph = []
#get distance -> weight
for i in range(n):
    for j in range(i+1, n):
        weight = dist(li[i][0], li[i][1], li[j][0], li[j][1])
        graph.append((i+1,j+1,weight))

for i in range(m):
    union(already[i][0], already[i][1])

graph.sort(key= lambda x: x[2]) #sorted by weight
ans = 0
#print(graph)
for edge in graph:
    x, y, z = edge
    if find(x) != find(y):
        union(x, y)
        ans += z

print(f"{ans:.2f}")