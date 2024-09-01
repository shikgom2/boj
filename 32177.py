import sys
input = sys.stdin.readline
import math

def dist(x1, y1, x2, y2):
    dist= math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return dist

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    parent[max(a, b)] = min(a, b)

n, k, t = map(int, input().split())
xp, yp, vp = map(int, input().split())
parent = [i for i in range(n + 1)]

li = []
li.append((0, xp, yp, vp, 0))

for c in range(1, n+1):
    x,y,v,p = map(int, input().split())
    li.append((c,x,y,v,p))

for i in range(len(li)):
    for j in range(len(li)):
        if(i == j):
            continue
    
        d = dist(li[i][1], li[i][2], li[j][1], li[j][2])
        if(d <= k and abs(li[j][3] - li[i][3]) <= t):
            union(li[i][0], li[j][0])

ans = []
for i in range(1, n+1):
    if(find(0) == find(i) and li[i][4] == 1):
        ans.append(i)
if(len(ans)):
    ans.sort()
    print(*ans, sep=" ")
else:
    print(0)