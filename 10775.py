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


ans = 0
n = int(input())
edges = []
parent = [i for i in range(n+1)]

t = int(input())
for _ in range(t):
    k = int(input())
    k = find(k)

    if(k != 0):
        union(k, k-1)
        ans += 1
    else:
        break
print(ans)