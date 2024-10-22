import sys
input = sys.stdin.readline 
from collections import deque

def bfs(x):
    ans = 1
    q = deque([x])
    visited[x] = True
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                ans += 1
    return ans
    
n,m = map(int, input().split())
graph = [[] for _ in range(n*n*50)]

for _ in range(m):
    x,y,a,b = map(int, input().split())
    x-= 1
    y -= 1
    a-=1
    b -=1
    graph[x*n+y].append(a*n+b)

#print(graph)

visited = [False] * (n*n*50)
ans = bfs(0)
print(ans)