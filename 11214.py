import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(u, p):
    if vis[u] > 0:
        return True
    vis[u] = 1
    for (v, e) in adj[u]:
        if e != p:
            if dfs(v, e):
                print(f'{u} {v}')
                return True
            else:
                print(f'{v} {u}')
    vis[u] = -1
    return False

n = int(input())
vis = [0] * (n + 1)
adj = [[] for _ in range(n + 1)]

li = []
for _ in range(n):
    parts = input().split()
    li.extend(parts)

li = list(map(int, li))

for i in range(0, len(li), 2):
    a = li[i]
    b = li[i + 1]
    index = i // 2
    adj[a].append((b, index))
    adj[b].append((a, index))

for u in range(1, n + 1):
    if vis[u] == 0:
        dfs(u, -1)
