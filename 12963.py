import sys
input = sys.stdin.readline

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x
def union(x, y):
    rx = find(x)
    ry = find(y)
    if rx == ry:
        return False
    if size[rx] < size[ry]:
        rx, ry = ry, rx
    parent[ry] = rx
    size[rx] += size[ry]
    return True

mod = 1000000007

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

parent = list(range(n))
size = [1] * n

pow3 = [1] * (m + 1)
for i in range(1, m + 1):
    pow3[i] = (pow3[i-1] * 3) % mod

ans = 0

for i in range(m-1,-1,-1):
    a, b = edges[i]
    
    ra = find(a)
    rb = find(b)
    if ra == rb:
        continue
    if (find(0) == ra and find(n-1) == rb) or (find(0) == rb and find(n-1) == ra):
        ans = (ans + pow3[i]) % mod
    else:
        union(a, b)
print(ans)
