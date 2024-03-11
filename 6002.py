import sys
input = sys.stdin.readline
INF = int(1e9)

def bellman_ford(s):
    dist[s] = -D
    for i in range(C):
        for j in range(e):
            cur = edges[j][1]
            next = edges[j][2]
            cost = edges[j][0]

            if(dist[cur] != INF and dist[next] > dist[cur] + cost):
                dist[next] = dist[cur] + cost
                if i == C - 1:
                    return True
    return False 

D,P,C,F,S = map(int, input().split())   #돈 간선 정점 제트기 수 시작
e = F + P
edges = []
dist = [INF] * (C + 1)

for i in range(P):
    x, y = list(map(int, input().split()))
    edges.append((-D, x, y)) 

for i in range(F):
    x, y, z = list(map(int,input().split()))
    edges.append((z - D, x, y))

if bellman_ford(S):
    print("-1")
else:
    i = min(dist)
    print(-i)