import sys
input = sys.stdin.readline
INF = int(1e9)

def bellman_ford(start):
    for i in range(v):
        for c, a, b in edges:
            if dist[b] > dist[a] + c:
                dist[b] = dist[a] + c
                if i == v - 1:
                    return True
    return False

N = int(input())
for _ in range(N):
    v, e, h = map(int, input().split())
    edges = []
    dist = [INF] * (v + 1)
    dist[1] = 0

    for _ in range(e):
        x, y, z = map(int, input().split())
        edges.append((z, x, y))

    for _ in range(h):
        x, y, z = map(int, input().split())
        edges.append((-z, x, y)) 

    flag = True
    for node in range(1, v+1):
        dist = [INF] * (v + 1)
        dist[node] = 0
        if bellman_ford(node):
            print("YES")
            flag = False
            break
    if(flag):
        print("NO")