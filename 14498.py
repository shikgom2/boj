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

V = 1001

graph = [[] for _ in range(V+1)]
d = [0] * (V+1)

n, m, v = map(int, input().split())

cat = []
dog = []

for i in range(v):
    a, b, c = map(int, input().split())
    if(c == 0):#c
        cat.append((a, b))
    else:
        dog.append((a, b))

for i in range(len(cat)):
    for j in range(len(dog)):
        if(cat[i][0] == dog[j][0] or cat[i][1] == dog[j][1]):
            graph[i+1].append(j+1)

ans = 0
for i in range(1, v + 1):
    c = [False] * (V+1)
    if dfs(i):
        ans += 1

print(ans)