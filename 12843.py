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

V = 2001
graph = [[] for _ in range(V+1)]
d = [0] * (V+1)

n, m = map(int, input().split())

check = [0] * (n+1)

for i in range(1, n + 1):
    k, s = map(str, input().split())
    if(s == 'c'):
        check[i] = 0
    elif(s == 's'):
        check[i] = 1

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    if check[a] == 1:
        a,b = b,a
    graph[a].append(b)

ans = 0
for i in range(1, n + 1):
    c = [False] * (V+1)
    if dfs(i):
        ans += 1

print(n-ans)