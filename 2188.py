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

graph = [[] for _ in range(201)]
d = [0] * 201

n, m = map(int, input().split())

for i in range(1, n + 1):
    s, *jobs = map(int, input().split())
    for j in jobs:
        graph[i].append(j)

ans = 0
for i in range(1, n + 1):
    c = [False] * 201
    if dfs(i):
        ans += 1

print(ans)