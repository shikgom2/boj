import sys
import math
sys.setrecursionlimit(10**5)

best = 0
ans = []

def df(cand, adj):

    m = len(cand)
    col = [0] * m
    res = 0
    for i in range(m):
        used = [False] * (m + 1)
        for j in range(i):
            if adj[cand[i]][cand[j]]:
                used[col[j]] = True
        c = 1
        while c <= m and used[c]:
            c += 1
        col[i] = c
        res = max(res, c)
    return res

def dfs(cand, clique, adj):
    global best, ans
    if len(clique) + df(cand, adj) <= best:
        return
    
    if not cand:
        if len(clique) > best:
            best = len(clique)
            ans = clique[:]
        return
    
    i = 0
    while i < len(cand):
        v = cand[i]
        newCand = []
        for j in range(i + 1, len(cand)):
            w = cand[j]
            if adj[v][w]:
                newCand.append(w)
        
        clique.append(v)
        dfs(newCand, clique, adj)
        clique.pop()
        
        cand.pop(i)
    
n, d = map(int, input().split())
li = []
idx = 2
for _ in range(n):
    x,y = map(int, input().split())
    li.append((x, y))
    idx += 2

adj = [[False]*n for _ in range(n)]
d2 = d*d

for i in range(n):
    x_i, y_i = li[i]
    for j in range(n):
        if i == j:
            continue
        x_j, y_j = li[j]
        dx = x_i - x_j
        dy = y_i - y_j
        if dx*dx + dy*dy <= d2 + 1e-9:
            adj[i][j] = True

cand = list(range(n))
clique = []

dfs(cand, clique, adj)

print(best)
if best > 0:
    print(" ".join(str(v+1) for v in ans))
else:
    print() 
