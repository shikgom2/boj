import sys
input = sys.stdin.readline
INF = int(1e9)

def bellman_ford():
      for i in range(v):
            for j in range(len(edges)):
                  cost, cur, next = edges[j]
                  if dist[next] > dist[cur] + cost:
                        dist[next] = dist[cur] + cost
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
        edges.append((z, y, x))
    for _ in range(h):
        x, y, z = map(int, input().split())
        edges.append((-z, x, y)) 

    if bellman_ford():
        print("YES")
    else:
        print("NO")