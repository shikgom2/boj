import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(now, root):
    global cnt
    visited[now] = cnt = cnt + 1
    num = visited[now]
    child = 0
    
    for next in graph[now]:
        if visited[next] == 0:
            child += 1
            low = dfs(next, False)
            num = min(low, num)
            if not root and low >= visited[now]:
                res[now] = True
        else:
            num = min(num, visited[next])
    
    if root and child > 1:
        res[now] = True
        
    return num

V, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]
cnt = 0

graph = [[] for _ in range(V + 1)]

for i, j in edges:
    graph[i].append(j)
    graph[j].append(i)

visited = [0] * (V+1)
res = [False] * 10001

for i in range(1, V+1):
    if(visited[i] == 0):
        dfs(i, True)

ans = sum(res[1:V+1])
print(ans)
for i in range(1, V + 1):
    if res[i]:
        print(i, end=" ")