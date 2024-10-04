import sys
input = sys.stdin.readline
from collections import defaultdict

# Constants
MAXN = 20001

# Graphs and other variables
edge = defaultdict(list)
redge = defaultdict(list)
order = [0] * MAXN
scc = [0] * MAXN
_in = [0] * MAXN
out = [0] * MAXN
vis = [False] * MAXN
idx = 0
n = 0

def sort(u):
    global idx
    vis[u] = True
    for v in edge[u]:
        if not vis[v]:
            sort(v)
    order[idx] = u
    idx -= 1

def findSCC(u):
    global idx
    vis[u] = True
    for v in redge[u]:
        if not vis[v]:
            findSCC(v)
    scc[u] = idx

def countDegree(size):
    for i in range(1, n + 1):
        for v in edge[i]:
            if scc[i] != scc[v]:
                out[scc[i]] += 1
                _in[scc[v]] += 1

def sol():
    global idx
    idx = n
    for i in range(1, n + 1):
        if not vis[i]:
            sort(i)

    for i in range(1, n + 1):
        vis[i] = False

    for i in range(1, n + 1):
        if not vis[order[i]]:
            idx += 1
            findSCC(order[i])

    if idx == 1:
        return 0

    countDegree(idx + 1)
    
    zeroIn = zeroOut = 0
    for i in range(1, idx + 1):
        if _in[i] == 0:
            zeroIn += 1
        if out[i] == 0:
            zeroOut += 1
            
    return max(zeroIn, zeroOut)

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    
    for i in range(n):
        edge[i].clear()
        redge[i].clear()
        _in[i] = out[i] = vis[i] = 0

    for _ in range(m):
        a, b = map(int, input().split())
        edge[a].append(b)
        redge[b].append(a)

    print(sol())