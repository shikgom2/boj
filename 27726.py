import sys
input = sys.stdin.readline
from collections import defaultdict

def find(a, i) :
    if a == parent[a][i] :
        return a
    parent[a][i] = find(parent[a][i], i)
    return parent[a][i]

def union(a, b, i) :
    pa, pb = find(a, i), find(b, i)
    if pa > pb:
            pa, pb = pb, pa
    parent[pb][i] = pa

n = int(input())
m = list(map(int, input().split()))

parent = [[i]*3 for i in range(n+1)]

for i in range(3):
    for _ in range(m[i]):
        a, b = map(int, input().split())
        union(a, b, i)
    
    for j in range(1, n+1):
        find(j, i)

parent = sorted([[tuple(parent[i]), i] for i in range(1, n+1)])
print(parent)

ans = []
tmp, prev = [parent[0][1]], parent[0][0]
print(tmp, prev)
for i in range(1, n) :
    if prev == parent[i][0] :   
        tmp.append(parent[i][1])
    else :  
        if len(tmp) > 1 :
            ans.append(sorted(tmp))
        tmp, prev = [parent[i][1]], parent[i][0]
if len(tmp) > 1 :
    ans.append(sorted(tmp))

print(len(ans))
for s in sorted(ans) :
    print(*s)