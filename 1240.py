from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, e):
    visited = [False] * (n + 1)
    distance = [0] * (n + 1) 

    q = deque([x])
    visited[x] = True
    while q:
        v = q.popleft()
        for i, cost in graph[v]: 
            if not visited[i]:
                q.append(i)
                visited[i] = True
                distance[i] = distance[v] + cost
                if i == e:
                    return distance[i]


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(n-1):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))
    graph[end].append((start, cost))

for _ in range(m):
    s,e = map(int, input().split())
    print(bfs(s, e))