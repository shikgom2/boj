import heapq

def floyd_warshall(graph):
    INF = int(1e9)
    n = len(graph)
    distance = [[INF] * n for _ in range(n)]

    for i in range(n):
        distance[i][i] = 0

    for i in range(n):
        for j, w in graph[i]:
            distance[i][j] = w

    for k in range(n):
        for i in range(n):
            for j in range(n):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    return distance

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]

for i in range(M):
    i,j,k = map(int, input().split())
    graph[i].append((j, k))
    '''
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))
    '''
ans = floyd_warshall(graph)

print(ans)
