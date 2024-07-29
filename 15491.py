import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5*2)

def query(l, r):
    if l > r:
        return 0
    len = r - l + 1
    L = log2[len]
    return max(sparse[l][L], sparse[r - (1 << L) + 1][L])

def dfs(i):
    stack = [(i, -1, 0)]
    dfsn = 0
    
    while stack:
        node, parent, state = stack.pop()
        if state == 0:  # 방문 시작
            par[node] = parent
            in_time[node] = dfsn
            dfsn += 1
            stack.append((node, parent, 1)) 
            for to in edges[node]:
                if to != parent:
                    stack.append((to, node, 0))
        else:
            out_time[node] = dfsn - 1

n = int(input())
li = list(map(int, input().split()))

edges = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edges[u].append(v)
    edges[v].append(u)

in_time = [0] * n
out_time = [0] * n
par = [-1] * n
dfsn = 0

dfs(0)

LOG = 20
log2 = [-1] * (n + 1)
i, k = 1, 0
while i <= n:
    log2[i] = k
    i <<= 1
    k += 1
for i in range(1, n + 1):
    if log2[i] == -1:
        log2[i] = log2[i - 1]

sparse = [[-1] * LOG for _ in range(n)]
for i in range(n):
    sparse[in_time[i]][0] = li[i]
for k in range(1, LOG):
    for i in range(n - (1 << k) + 1):
        sparse[i][k] = max(sparse[i][k - 1], sparse[i + (1 << (k - 1))][k - 1])

ans = 0
for i in range(n):
    ret = 0
    for to in edges[i]:
        if to == par[i]:
            continue
        ret += query(in_time[to], out_time[to])

    if par[i] != -1:
        ret += max(query(in_time[0], in_time[i] - 1), query(out_time[i] + 1, out_time[0]))
    ans = max(ans, ret)

print(ans)
