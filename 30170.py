import sys
input = sys.stdin.readline

n, m = map(int, input().split())
edges = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)
    
for i in edges:
    i.sort()

d = {}
mod = (1 << 61) - 1
base = 10**9 + 7
for i in range(n):
    h = 0
    for j in edges[i]:
        h *= base
        h += j + 1
        h %= mod

    if h not in d:
        d[h] = []
    d[h].append(i)

    if len(d) > 3:
        print(-1)
        exit()

cnt = [0] * n
for i in d.values():
    for j in edges[i[0]]:
        cnt[j] += 1

if min(cnt) <= 2 <= max(cnt):
    ans = [0] * n
    for idx, i in enumerate(d.values()):
        for j in i:
            ans[j] = idx + 1
    print(*ans)
else:
    print(-1)