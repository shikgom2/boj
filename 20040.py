import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x
        return False
    else:
        return True

def same(x, y):
    return find(x) == find(y)
    
m, n = map(int, input().split())
parent = [i for i in range(m + 1)]
res = 0
cycle_exists = False
for i in range(n):
    x, y = map(int, input().split())
    if union(x, y):
        cycle_exists = True
        res = i
        break

if cycle_exists:
    print(res+1)
else:
    print(0)