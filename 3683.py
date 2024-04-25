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

t = int(input())
for _ in range(t):
    graph = [[] for _ in range(V+1)]
    d = [0] * (V+1)

    n, m, v = map(int, input().split())

    cat = []
    dog = []

    for i in range(v):
        win, lose = map(str, input().split())
        if(win[0] == 'C'):#c
            cat.append((win, lose))
        else:
            dog.append((win, lose))

    print(cat)
    print(dog)

    for i in range(len(cat)):
        for j in range(len(dog)):
            if(cat[i][0] == dog[j][1] or cat[i][1] == dog[j][0]) and j+1 not in graph[i+1]:
                graph[i+1].append(j+1)

    ans = 0
    for i in range(1, v + 1):
        c = [False] * (V+1)
        if dfs(i):
            ans += 1

    print(v - ans)