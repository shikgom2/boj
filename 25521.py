import sys
input = sys.stdin.readline

from collections import defaultdict

def dfs(node, depth):
    global ans
    if v[node] == M:
        ans = depth
    
    for neighbor in adj[node]:
        dfs(neighbor, depth + 1)

N, M = map(int, input().split())

adj = defaultdict(list)

for _ in range(N - 1):
    a, b = map(int, input().split())
    adj[a].append(b)

v = list(map(int, input().split()))

ans = -1
dfs(0, 0)

print(ans)