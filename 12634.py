
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

def dom(a, b):
    for i in range(len(a)):
        if a[i] >= b[i]:
            return False
    return True

t = int(input())

for test in range(t):

    V = 1000
    graph = [[] for _ in range(V+1)]
    d = [0] * (V+1)

    n, k = map(int, input().split())
    c = [[0] * k for _ in range(n)]
    for i in range(n):
        c[i] = list(map(int, input().split()))

    ret = 0
    for i in range(n):
        for j in range(n):
            for k in range(k):
                if(c[i][k] <= c[j][k]):
                    break
            if(k == k-1):
                graph[i][j] = 1

    ans = 0
    for i in range(1, n + 1):
        c = [False] * (V+1)
        if dfs(i):
            ans += 1

    print("Case #{}: {}".format(test + 1, ans))
