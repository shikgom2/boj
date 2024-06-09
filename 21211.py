import heapq
import math
import sys
input = sys.stdin.readline
from collections import defaultdict

sys.setrecursionlimit(200000)

maxn = 200010

head = [-1] * maxn
e = [0] * maxn
ne = [0] * maxn
w = [0] * maxn
d = [0] * maxn
vis = [0] * maxn
sz = 0

def add(u, v, ww):
    global sz
    e[sz] = v
    w[sz] = ww
    ne[sz] = head[u]
    head[u] = sz
    sz += 1

def dijkstra():
    global d, vis
    d = [float('inf')] * maxn
    d[0] = 0
    q = [(0, 0)]
    while q:
        du, u = heapq.heappop(q)
        if vis[u]:
            continue
        vis[u] = 1
        j = head[u]
        while j != -1:
            v = e[j]
            if d[v] > d[u] + w[j]:
                d[v] = d[u] + w[j]
                heapq.heappush(q, (d[v], v))
            j = ne[j]

sz = 0
head = [-1] * maxn
n, m, l, u = map(int, input().split())
for _ in range(m):
    x, y, z = map(int, input().split())
    add(x, y, z)
    add(y, x, z)
dijkstra()
ans = 0
vis = [0] * maxn
for i in range(n):
    if(d[i] <= (u - 1) / 2):
        j = head[i]
        while(j != -1):
            if (not vis[j]) and (not vis[j ^ 1]):
                vis[j] = vis[j ^ 1] = 1
                ans += 1
            j = ne[j]
print(ans)