import sys
input = sys.stdin.readline
from collections import deque

def bfs(x):
    q = deque([x])
    visited[x] = True
    ans = 1
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                ans += 1
                visited[i] = True

    return ans

n, m, k = map(int, input().split())

parent = [i for i in range(n + 1)]
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    
    if(i != k-1):
        graph[a].append(b)
        graph[b].append(a)

visited = [False] * (n+1)

li = []
res = 1
ans = 0
for i in range(n):
    if(len(graph[i]) >= 1 and visited[i] == False ):
        ans = bfs(i)

        if(ans == n):
            res = 0
        else:
            res *= ans
print(res)