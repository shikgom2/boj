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

V = 501
n, m, k1, k2 = map(int, input().split())

#my team
graph = [[] for _ in range(V+1)]
d = [0] * (V+1)

for i in range(1, k1 + 1):
    a,b = map(int,input().split())
    graph[a].append(b)

ans = 0
for i in range(1, n+1):
    c = [False] * (V+1)
    if dfs(i):
        ans += 1

#enemy team
graph = [[] for _ in range(V+1)]
d = [0] * (V+1)

for i in range(1, k2 + 1):
    a,b = map(int,input().split())
    graph[a].append(b)

ans1 = 0
for i in range(1, n + 1):
    c = [False] * (V+1)
    if dfs(i):
        ans1 += 1

if(ans < ans1):
    print("네 다음 힐딱이")
else:
    print("그만 알아보자")