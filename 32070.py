import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(start):
    stack = [start]
    vis[start] = 1
    tmp.append(start)
    
    while stack:
        u = stack.pop()
        for v in graph[u]:
            if not vis[v]:
                vis[v] = 1
                tmp.append(v)
                stack.append(v)
                
n = int(input())
out_degree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(n):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    out_degree[b] += 1

vis = [0] * (n + 1)
ans = 0

for i in range(1, n + 1):
    if not vis[i]:
        tmp = []
        dfs(i)

        if len(tmp) == 1:
            continue
        
        cnt = sum(1 for u in tmp if out_degree[u] >= 2)

        if cnt >= 2:
            print(-1)
            exit()

        ans += len(tmp) + 1

print(ans)