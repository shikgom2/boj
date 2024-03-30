import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(now, parent):
    global cnt
    visited[now] = cnt = cnt + 1
    num = visited[now]
    child = 0
    
    for next in graph[now]:
        if next == parent:
            continue

        if not visited[next]:
            low = dfs(next, now)
            if low > visited[now]:
                ans.append((min(now, next), max(now, next)))
            num = min(num, low)
        else:
            num = min(num, visited[next])

    return num

def dfs1(x, visited, order):
    visited[x] = True
    order.append(x)

    for node in graph[x]:
        if not visited[node]:
            dfs1(node, visited, order)

    return order

N = int(input())

for _ in range(N):
    
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    cnt = 0
    ans = []

    graph = [[] for _ in range(V + 1)]

    for i, j in edges:
        graph[i].append(j)
        graph[j].append(i)

    visited = [0] * (V+1)
    res = [False] * 10001

    dfs(1, 0)
    ans.sort()
    print(ans)

    if(len(ans) == 0):
        print("YES")
        visited = [False] * (V+1)
        order = []
        res = dfs1(1, visited, order)

        print(res)
    else:
        print("NO")
