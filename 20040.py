def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    parent[y] = x

n, t = map(int, input().split())
parent = [i for i in range(n)]
ans = 0

for i in range(t):
    a, b = map(int, input().split())
    if find(a) == find(b):
        if ans == 0:
            ans = i + 1
    else:
        union(a, b)

print(ans)