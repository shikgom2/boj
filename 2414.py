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

V = 50
graph = [[] for _ in range(V+1)]
d = [0] * (V+1)

n, m = map(int, input().split())

for k in range(1,m +1):
    li = list(map(str, input().strip()))
    for i in range(len(li)):
        if(li[i] == '*'):
            graph[k].append(i+1)
ans = 0

#print(graph)
for i in range(1, n + 1):
    c = [False] * (V+1)
    if dfs(i):
        ans += 1

print(ans)