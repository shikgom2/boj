import sys
input = sys.stdin.readline

res = []

def dfs(v, num):
  num += 1
  visited[v] = True

  if v == b:
    res.append(num)

  for i in graph[v]:
    if not visited[i]:
      dfs(i, num)

V = int(input())
a, b = map(int, input().split())
E = int(input())

edges = [list(map(int, input().split())) for _ in range(E)]
visited = [False] * (V+1)
graph = [[] for _ in range(V + 1)]

for i, j in edges:
    graph[i].append(j)
    graph[j].append(i)

idx = 0
dfs(a, idx)

if len(res) == 0:
  print(-1)
else:
  print(res[0]-1)