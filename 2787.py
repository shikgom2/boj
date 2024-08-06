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

V = 1000
graph = [[] for _ in range(V+1)]
d = [0] * (V+1)

n, m = map(int, input().split())

#query
for i in range(m):
    li = list(map(int, input().split()))
    
    if(li[0] == 1):
        
    else(li[0] == 2):
        

#query에 해당 x, matching
ans = 0
for i in range(1, n + 1):
    c = [False] * (V+1)
    if dfs(i):
        ans += 1

print(ans)