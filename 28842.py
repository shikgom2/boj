
import sys
input = sys.stdin.readline
sys.setrecursionlimit(155757)

def dfs(u):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            dfs(v)
    order.append(u)


def dfs_interval(u):
    visited[u] = True
    in_time[u] = time[0]
    time[0] += 1
    for v in graph[u]:
        if not visited[v]:
            dfs_interval(v)
    out_time[u] = time[0]
    time[0] += 1

n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)

# Perform topological sort
visited = [False] * n
order = []

for i in range(n):
    if not visited[i]:
        dfs(i)

order.reverse()

in_time = [0] * n
out_time = [0] * n
time = [0] 

visited = [False] * n

for u in order:
    if not visited[u]:
        dfs_interval(u)

# Check for overlapping intervals
# Build the parent list
parent = [-1] * n
stack = []  # Stack to keep track of current ancestors

for u in order:
    # Pop ancestors that are not proper ancestors
    while stack and not (in_time[stack[-1]] < in_time[u] and out_time[u] < out_time[stack[-1]]):
        stack.pop()
    if stack:
        parent[u] = stack[-1]
    stack.append(u)

# Verify that intervals are nested properly
flag = True
for u in range(n):
    for v in graph[u]:
        if not (in_time[u] < in_time[v] and out_time[v] < out_time[u]):
            flag = False
            break
    if not flag:
        break

if not flag:
    print("No")
    exit()

print("Yes")
for i in range(n):
    if parent[i] == -1:
        print(-1, end=' ')
    else:
        print(parent[i] + 1, end=' ')
print()