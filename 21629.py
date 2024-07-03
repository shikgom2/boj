from collections import deque, defaultdict

maxn = int(1e5) + 5
n, m = 0, 0
dis = [0] * maxn
cnt = [0] * maxn
vis = [0] * maxn
G = defaultdict(list)

# Read input
n, m = map(int, input().split())
for _ in range(m):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

q = deque([1])
vis[1] = 1

while q:
    u = q.popleft()
    for v in G[u]:
        if dis[u] == 1:
            cnt[v] += 1
        if vis[v]:
            continue
        dis[v] = dis[u] + 1
        vis[v] = 1
        q.append(v)

ans = 0
for i in range(1, n + 1):
    if dis[i] and dis[i] <= 2:
        ans += 1 * cnt[i] * (cnt[i] - 1)

print(ans)