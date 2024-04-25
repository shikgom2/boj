import sys
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

V = 300
graph = [[] for _ in range(V+1)]
d = [0] * (V+1)

n, m, k = map(int, input().split())

for i in range(1, n+1):
    for j in range(1, m+1):
        graph[i].append(j)

for i in range(k):
    a, b = map(int, input().split())
    if b in graph[a]:
        graph[a].remove(b)

ans = 0
for i in range(1, n + 1):
    c = [False] * (V+1)
    if dfs(i):
        ans += 1

print(ans)