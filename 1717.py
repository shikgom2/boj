import sys
input = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[y]=x

def same(x, y):
    if find(x) != find(y):
        return False
    else:
        return True
    
m, n = map(int, input().split())
parent = [i for i in range(m + 1)]

result = []
for i in range(n):
    z, x, y = map(int, input().split())
    
    if(z == 0):
        union(x, y)
    elif(z == 1):
        if same(x, y):
            result.append("YES")
        else:
            result.append("NO")

for res in result:
    print(res)