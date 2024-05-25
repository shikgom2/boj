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

t = int(input())
for _ in range(t):
    V = 1000
    graph = [[] for _ in range(V+1)]
    d = [0] * (V+1)

    n, m = map(int, input().split())

    for i in range(m):
        u, v = map(int, input().split())
        graph[u+1].append(v+1)

    ans = 0
    for i in range(1, n + 1):
        c = [False] * (V+1)
        if dfs(i):
            ans += 1

    print(ans)