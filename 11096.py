import sys
input = sys.stdin.readline
from math import sqrt

N = 205

class Node:
    def __init__(self, x, y, r, id):
        self.x = x
        self.y = y
        self.r = r
        self.id = id

def dis(x, y):
    return x * x + y * y

def solve():
    global graph, s, t, n
    for i in range(n):
        x, r, id = p[i].x, p[i].r, p[i].id
        if x - r <= 0 and 0 <= x + r:
            graph[s].append(id)
        if x - r <= 200 and 200 <= x + r:
            graph[id].append(t)

    for i in range(n):
        for j in range(i + 1, n):
            if dis(p[i].x - p[j].x, p[i].y - p[j].y) <= dis(p[i].r + p[j].r, 0):
                graph[p[i].id].append(p[j].id)
                graph[p[j].id].append(p[i].id)

def dfs(u, length):
    global vis
    vis[u] = True
    for v in graph[u]:
        if v != t and v > length or vis[v]:
            continue
        dfs(v, length)

def ok(length):
    global vis
    vis = [False] * N
    dfs(s, length)
    return vis[t]


n = int(input())
graph = [[] for _ in range(N)]
p = []

for i in range(n):
    x, y, r = map(int, input().split())
    p.append(Node(x, y, r, i + 1))

s = 0
t = n + 1
solve()

ans = 0
for i in range(1, n + 1):
    if ok(i):
        ans = i - 1
        break

print(ans)