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
li = list(map(int, input().split()))

parent = [i for i in range(k + 1)]

for _ in range(m):
    a,b = map(int, input().split())
    if(find(b) != a):
        union(a,b)
    else:
        parent[a] = b

print(parent)
    