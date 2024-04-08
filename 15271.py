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

V = 10001
graph = [[] for _ in range(V+1)]
d = [0] * (V+1)

m,n = map(int, input().split())

for i in range(1, n + 1):
    a,b = map(int, input().split())
    if(a%2 == 0 and b%2 == 0):
        continue
    if(a%2 == 1 and b%2 == 1):
        continue
    if(a%2 == 0 and b%2 == 1):
        tmp = a
        a = b
        b = tmp
        graph[a].append(b)
    if(a%2 == 1 and b%2 == 0):
        graph[a].append(b)

ans = 0
for i in range(1, m + 1):
    c = [False] * (V+1)
    if dfs(i):
        ans += 1

if(ans*2 < m):
    ans = ans * 2 + 1
else:
    ans = ans * 2
print(ans)