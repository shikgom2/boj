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

n,m,k = map(int, input().split())

#making MST, red edge give weight inf?
#like greedy.

edges = []
parent = [i for i in range(n + 1)]

for _ in range(m):
    li = list(map(str, input().split()))
    edges.append((li[0], int(li[1]), int(li[2])))

#maximum spanning tree (blue weight 0)
graph = []
for i in range(m):
    if(edges[i][0] == 'B'):
        graph.append((0, edges[i][1], edges[i][2]))
    else: #red
        graph.append((1, edges[i][1], edges[i][2]))

graph.sort()

max_ans = 0
for edge in graph:
    z,x,y = edge
    if find(x) != find(y):
        union(x, y)
        if(z == 0):
            max_ans += 1

#minimum spanning tree (blue weight 1)
graph = []
for i in range(m):
    if(edges[i][0] == 'B'):
        graph.append((1, edges[i][1], edges[i][2]))
    else: #red
        graph.append((0, edges[i][1], edges[i][2]))

graph.sort()
parent = [i for i in range(n + 1)]
min_ans = 0
for edge in graph:
    z,x,y = edge
    if find(x) != find(y):
        union(x, y)
        if(z == 1):
            min_ans += 1

if(min_ans <= k and k <= max_ans):
    print(1)
else:
    print(0)