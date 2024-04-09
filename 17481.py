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

V = 2002
graph = [[] for _ in range(V+1)]
dir = []

d = [0] * (V+1)

n, m = map(int, input().split())


for _ in range(m):
    character = input().rstrip()
    dir.append(character)

#print(dir)
for k in range(n):
    li = []
    li = list(map(str, input().split()))

    for i in range(1, len(li)):
        for j in range(len(dir)):
            if(dir[j] == li[i]):
                graph[k+1].append(j+1)

#print(graph)
ans = 0
for i in range(1, n + 1):
    c = [False] * (V+1)
    if dfs(i):
        ans += 1

if(ans == n):
    print("YES")
else:
    print("NO")
    print(ans)