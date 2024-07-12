import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, e):
    q = deque([(x,0)])
    visited[x] = True
    while q:
        v, cnt = q.popleft()
        
        for i in graph[v]:
            if not visited[i]:
                if(i == e):
                    return cnt+1   
                q.append((i, cnt+1))
                visited[i] = True
    return 0

n,m,k = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e = map(int, input().split())

    graph[s].append(e)
    graph[e].append(s)


for _ in range(k):
    visited = [False for _ in range(n+1)]
    s, e, d = map(int, input().split())

    if(s == e):
        print("TAK")
    else:
        ans = bfs(s,e) #s->e
        print("ans : " , ans)
        if(ans == 0 or ans > d): #ans = 0 or d까지 도달불가
            print("NIE")
        elif(ans % 2 and d % 2): #even
            print("TAK")
        elif(ans % 2 == 0 and d % 2 == 0):
            print("TAK")
        else:
            print("NIE")