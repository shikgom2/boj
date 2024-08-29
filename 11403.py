import sys
input = sys.stdin.readline
INF = float('inf')

#n^3
def floyd_warshall(graph):
    V = len(graph)

    # 거리 행렬 초기화
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


n = int(input())
graph = [[INF] * n for _ in range(n)]

for i in range(n):
    li = list(map(int, input().split()))
    for j in range(len(li)):
        if(li[j] == 1):
            graph[i][j] = 1
print(graph)
ans = floyd_warshall(graph)
print(ans)
for i in range(n):
    for j in range(n):
        if(ans[i][j] != INF):
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()