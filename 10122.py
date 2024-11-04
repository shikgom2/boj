import sys
input = sys.stdin.readline

def dfs(x, p, d):
    depth[d] += 1
    tmp = d
    for i in graph[x]:
        if i != p:
            tmp = max(tmp, dfs(i, x, d + 1))
    return tmp

def solve(v):
    pref, suff = 0, sum(v)
    result = 0
    for i in v:
        suff -= i
        result += i * pref * suff
        pref += i
    return result

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

depth = [0] * (n + 1)

ans = 0
v = {}

for i in range(1, n + 1):
    for j in graph[i]:
        len_d = dfs(j, i, 1)
        for k in range(1, len_d + 1):
            if k not in v:
                v[k] = []
            v[k].append(depth[k])
            depth[k] = 0
    for j in range(1, n + 1):
        if j in v and v[j]:
            ans += solve(v[j])
            v[j].clear()

print(ans)