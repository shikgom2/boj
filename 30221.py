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

v, e = map(int, input().split())
edges = []
dist = [INF] * (v + 1)
dist[1] = 0

for _ in range(e):
    x, y, t, z = map(str, input().split())
    x = int(x)
    y = int(y)
    z = int(z)

    if(t == 'b'):         
        edges.append((z, x, y))
    elif(t == 'r'):
        edges.append((-z, x, y))
bellman_ford()

for i in range(2, v + 1):
    if dist[i] < 0:
        print(i)