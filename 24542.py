import sys
input = sys.stdin.readline
from collections import deque

def bfs(x):
    q = deque([x])
    visited[x] = True
    cnt = 1
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                cnt += 1
                visited[i] = True

    return cnt

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m): 
    a, b= map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)
ans = []
for i in range(1, n+1):
    if(visited[i] == False):
        s = bfs(i)
        ans.append(s)

res = 1
mod = 10 ** 9 + 7
for i in range(len(ans)):
    res = (res * ans[i]) % mod

print(res % mod)