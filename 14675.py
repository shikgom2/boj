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

def dfs2(now, parent):
    global cnt
    visited[now] = cnt = cnt + 1
    num = visited[now]
    child = 0
    
    for next in graph[now]:
        if next == parent:
            continue

        if not visited[next]:
            low = dfs(next, now)
            if low > visited[now]:
                ans.append((min(now, next), max(now, next)))
            num = min(num, low)
        else:
            num = min(num, visited[next])

    return num

V = int(input())
E = V-1
edges = [list(map(int, input().split())) for _ in range(E)]
cnt = 0
ans = []

graph = [[] for _ in range(V + 1)]

temp = []
for i, j in edges:
    graph[i].append(j)
    temp.append((i,j))

visited = [0] * (V+1)
res = [False] * 100001

for i in range(1, V+1):
    if(visited[i] == 0):
        dfs(i, True)

points = []
for i in range(1, V + 1):
    if res[i]:
        points.append(i)


cnt = 0
visited = [0] * (V+1)
res = [False] * 100001

dfs(1, 0)

i = int(input())
for _ in range(i):
    a,b = map(int, input().split())

    if(a == 1):
        if(b in points):
            print("yes")
        else:
            print("no")
    if(a == 2):
        ansi, ansj = temp[b-1]
        flag = True
        for a in ans:
            if(a[0] == ansi and a[1] == ansj):
                flag = False
        
        if(flag):
            print("yes")
        else:
            print("no")