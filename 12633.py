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

for ttt in range(t):

    n, m = map(int, input().split())

    V = n*2+1
    graph = [[] for _ in range(V+1)]
    d = [0] * (V+1)
    
    li = []
    for _ in range(n):
        l = list(map(int, input().split()))
        li.append(l)

    for i in range(n):
        for j in range(n):
            if(i == j):
                continue
            ok = True

            for k in range(m):
                if(li[j][k] >= li[i][k]):
                    ok = False
        
            if(ok):
                graph[i+1].append(n+j+1)
                graph[n+j+1].append(i+1)

    ans = 0
    for i in range(1, n + 1):
        c = [False] * (V+1)
        if dfs(i):
            ans += 1

    print("Case #{}: {}".format(ttt + 1, n - ans))
