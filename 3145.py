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

V = 51
graph = [[] for _ in range(V+1)]
d = [0] * (V+1)

map = [[] for _ in range(51)]

i, j = list(map(int, input().split()))

for _ in range(i):
    map[i] = list(map(str, input().split()))


print(map)
'''
ans = 0
for i in range(1, n+ 1):
    c = [False] * (V+1)
    if dfs(i):
        ans += 1

print(ans)
'''