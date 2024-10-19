import sys
input = sys.stdin.readline
import copy

def dfs(x):
    global ans
    
    visited[x] = True
    if(len(tmp[x]) == 0):
        ans += 1
        
    for node in tmp[x]:
        if not visited[node]:
            dfs(node)

n = int(input())
li = list(map(int, input().split()))

graph = [[] * (n+1) for _ in range(n+1)]

root = -1
for i in range(len(li)):
    if(li[i] == -1):
        root = i
        continue
    else:
        graph[li[i]].append(i)

tmp = copy.deepcopy(graph)

k = int(input())
if(k == root):
    print(0)
    exit()
    
for i in range(n):
    for j in range(len(graph[i])):
        if(graph[i][j] == k):
            tmp[i].remove(k)

ans = 0
visited = [False] * (n+1)
dfs(root)

print(ans)