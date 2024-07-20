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
parent = [i for i in range(n + 1)]

for _ in range(m):
    a, b=  map(int, input().split())
    union(a,b)

li = list(map(int, input().split()))
ans = 0

for i in range(n-1):
    if(find(li[i]) != find(li[i+1])):
        ans += 1
print(ans)