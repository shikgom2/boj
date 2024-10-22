import sys
input = sys.stdin.readline 
from collections import deque
sys.setrecursionlimit(155557)

def dfs(node, parent = - 1):
    visited[node] = True
    ret = (node, 1)
    for i in graph[node]:
        if i != parent:
            csol = dfs(i, node)
            csol = (csol[0], csol[1] + 1)
            if csol[1] > ret[1]:
                ret = csol
    return ret

def radius(node):
    s1 = dfs(node)
    return dfs(s1[0])[1]

n,m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
ans = 0
visited = [False] * (n+1)

for i in range(1, n+1):
    if(visited[i] == False):
        ans+=radius(i)

print(ans)