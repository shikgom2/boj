import sys
input = sys.stdin.readline
from collections import deque

def bfs(x):
    q = deque([x])
    visited[x] = True
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
t = int(input())
for _ in range(t):
    n = int(input())
    m = int(input())

    graph = [[] for _ in range(n+1)]

    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (n+1)
    ans = 0
    for i in range(1, n+1):
        if(visited[i] == False):
            bfs(i)
            ans += 1

    if(n == m+1 and ans == 1):
        print("tree")
    else:
        print("graph")