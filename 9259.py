import sys
input = sys.stdin.readline
from collections import deque


N,M,K = map(int, input().split())

W = int(int(input()))

dic = {}
for _ in range(W):
    u,s = map(str, input().split())
    u = int(u)
    if s not in dic:
        dic[s] = []
    dic[s].append(u)

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

source = [0] * (N + 1)
dis = [0] * (N + 1)
mark = [0] * (N + 1)
cur = 0

for name, nodes in dic.items():
    if len(nodes) < 2:
        continue
    
    cur += 1
    q = deque()

    for node in nodes:
        mark[node] = cur
        source[node] = node
        dis[node] = 0
        q.append(node)
    
    while q:
        cur = q.popleft()
        cur_src = source[cur]
        cur_dist = dis[cur]
        if cur_dist < K:
            for nb in graph[cur]:
                if mark[nb] != cur:
                    mark[nb] = cur
                    source[nb] = cur_src
                    dis[nb] = cur_dist + 1
                    q.append(nb)
                elif source[nb] != cur_src:
                    if cur_dist + dis[nb] + 1 <= K:
                        print("POWERFUL CODING JungHwan")
                        exit()
print("so sad")
