import sys
import math
input = sys.stdin.readline

def dfs(x):
    for i in range(len(graph[x])):
        t = graph[x][i]
        if c[t]:
            continue
        c[t] = True
        if d[t] == 0 or dfs(d[t]):
            d[t] = x
            return True
    return False

V = 1000
graph = [[] for _ in range(V+1)]
d = [0] * (V+1)

n,m,v = map(int, input().split())

rat = []
for _ in range(n):
    i,j = map(float, input().split())
    rat.append((i,j))
hole = []
for _ in range(m):
    i,j = map(float, input().split())
    hole.append((i,j))

for i in range(n):
    for j in range(m):
        x1 = rat[i][0]
        y1 = rat[i][1]
        x2 = hole[j][0]
        y2 = hole[j][1]
        #print(x1, y1, x2, y2)
        dx = x2 - x1
        dy = y2 - y1

        if ((x1 - x2)**2 + (y1 - y2)**2) **0.5 <= s*v:
            graph[i+1].append(j+1)

ans = 0
for i in range(1, n + 1):
    c = [False] * (V+1)
    if dfs(i):
        ans += 1

print(n-ans)