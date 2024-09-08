import sys
input = sys.stdin.readline
from collections import deque

maxn = 110
N = 1010
M = 10010
inf = float('inf')

class Edge:
    def __init__(self, v, w):
        self.v = v
        self.w = w

def spfa(n, e, dis, sum_, vis):
    sum_[1] += 1
    dis[1] = 0
    que = deque([1])
    
    while que:
        u = que.popleft()
        vis[u] = False
        
        for edge in e[u]:
            v = edge.v
            if dis[v] > dis[u] + edge.w:
                dis[v] = dis[u] + edge.w
                if not vis[v]:
                    if sum_[v] + 1 > n:
                        return -1
                    que.append(v)
                    vis[v] = True
                    sum_[v] += 1
    
    return -2 if dis[n] == inf else dis[n]


n, ml, md = map(int, input().split())

e = [[] for _ in range(n + 1)]
vis = [False] * (n + 1)
dis = [inf] * (n + 1)
sum_ = [0] * (n + 1)

for _ in range(ml):
    a, b, d = map(int, input().split())
    e[a].append(Edge(b, d))

for _ in range(md):
    a, b, d = map(int, input().split())
    e[b].append(Edge(a, -d))

for i in range(1, n):
    e[i + 1].append(Edge(i, 0))

print(spfa(n, e, dis, sum_, vis))
