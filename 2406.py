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

n,m = map(int, input().split())

edges = []
parent = [i for i in range(n + 1)]

for i in range(m):
    s, e = map(int, input().split())
    edges.append((s, e, 0))
    edges.append((e, s, 0))
    union(s,e)
    
cost = [[0] * n for _ in range(n)]

for i in range(1, n+1):
    li = list(map(int, input().split()))

    for j in range(len(li)):        
        if(i == 1 or j == 0):
            continue
        edges.append((i, j+1, li[j]))

edges.sort(key=lambda x: x[2])

#print(edges)

ans = 0
ans_cost = 0 
ans_li = []

for edge in edges:
    x,y,z = edge
    if find(x) != find(y):
        union(x, y)
        ans += 1
        ans_cost += z
        ans_li.append((x,y))
        
print(ans_cost, ans)
for i in range(len(ans_li)):
    print(f"{ans_li[i][0]} {ans_li[i][1]}")