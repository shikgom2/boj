import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(index):
    visited[index] = True
    for idx in graph[index]:
        if not visited[idx]:
            dfs(idx)
    queue.append(index)

def reverse_dfs(index):
    visited[index] = True
    ids[index] = idx
    for _idx in reverse_graph[index]:
        if not visited[_idx]:
            reverse_dfs(_idx)

N, M = map(int, input().split())
graph = [[] for __ in range(N + 1)]
reverse_graph = [[] for __ in range(N + 1)]
for __ in range(M):
    x, y = map(int, input().split())
    graph[x+1].append(y+1)
    reverse_graph[y+1].append(x+1)

queue = []
visited = [False] * (N + 1)
for here in range(1, N + 1):
    if not visited[here]:
        dfs(here)

visited = [False] * (N + 1)
ids = [-1] * (N + 1)
idx = 0
while queue:
    here = queue.pop()
    if not visited[here]:
        reverse_dfs(here)
        idx += 1

ind = [0] * idx
for here in range(1, N + 1):
    for there in graph[here]:
        if ids[here] != ids[there]:
            ind[ids[there]] += 1 
answer = 0
for i in range(idx):
    if not ind[i]:
        answer += 1
print(answer)
