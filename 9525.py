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

V = 101
graph = [[] for _ in range(V+1)]
d = [0] * (V+1)

n = int(input())

for i in range(n):
    li = list(map(str, input().strip()))
    print(li)

    for j in range(len(li)):
        if(li[j] == '.'):
            graph[i+1].append(j+1)

#print(graph)

ans = 0
for i in range(1, n + 1):
    c = [False] * (V+1)
    if dfs(i):
        ans += 1

print(ans)