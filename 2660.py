import sys
input = sys.stdin.readline
from collections import deque

def bfs(x):
    q = deque([(x, 0)])
    visited[x] = True
    
    while q:
        idx, t = q.popleft()
        for i in graph[idx]:
            if not visited[i]:
                q.append((i, t+1))
                visited[i] = True
                cost[i] = t+1

    
n = int(input())
graph = [[] * (n+1) for _ in range(n+1)]

while(True):
    a,b = map(int, input().split())
    if(a == -1 and b == -1):
        break
    graph[a].append(b)
    graph[b].append(a)


depth = 1000000
ans_li = []
for i in range(1, n+1):
    visited = [False] * (n+1)
    cost = [0] * (n+1)

    bfs(i)
    
    if(depth > max(cost)):
        ans_li = []
        ans_li.append(i)
        depth = max(cost)
    elif(depth == max(cost)):
        ans_li.append(i)
        
print(depth, len(ans_li))
print(*ans_li)