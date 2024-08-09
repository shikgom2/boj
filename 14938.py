import sys
input = sys.stdin.readline

INF = float('inf')

#n^3
def floyd_warshall(graph):
    V = len(graph)
    dist = [[INF] * V for _ in range(V)]

    for i in range(V):
        for j in range(V):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j] != 0:
                dist[i][j] = graph[i][j]

    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

n,m,r = map(int, input().split())
li = list(map(int, input().split()))

graph = [[INF] * n for _ in range(n)]
for _ in range(r):
    s, e ,w = map(int, input().split())
    graph[s-1][e-1] = w
    graph[e-1][s-1] = w

for i in range(n):
    graph[i][i] = 0

g = floyd_warshall(graph)
ans = 0

for i in range(n):
    tmp = 0
    for j in range(n):
        if(g[i][j] <= m):
            tmp += li[j]
    ans = max(ans, tmp)
print(ans)