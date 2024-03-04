import sys
input = sys.stdin.readline
INF = int(1e9)

def bellman_ford(s):
    dist[s] = 0
    for i in range(v):
        for j in range(e):
            cur = edges[j][1]
            next = edges[j][2]
            cost = edges[j][0]


            if(dist[cur] != INF and dist[next] > dist[cur] + cost):
                dist[next] = dist[cur] + cost
                if i == v - 1:
                    return True

    return False

v, e = map(int, input().split())
edges = []
dist = [INF] * (v + 1)

for _ in range(e):
    x, y, z = map(int, input().split())
    edges.append((z, x, y))

if bellman_ford(1):
    print("-1")
else:
    for i in range(2, v + 1):
        if dist[i] == INF:
            print("-1")
        else:
            print(dist[i])