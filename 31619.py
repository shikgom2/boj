import sys
input = sys.stdin.readline
import bisect
n,m, q = map(int, input().split())

li = [map(int, input().split()) for i in range(n)]
p, a = map(list, zip(*li))
a = [t - 1 for t in a]

prefix = [0] * (n + 1)
for i in range(n):
    prefix[i + 1] = prefix[i] + p[i]
idx = [[] for i in range(n)]
sum = [[0] for i in range(n)]

for i in range(n):
    idx[a[i]].append(i)
    sum[a[i]].append(sum[a[i]][-1] + a[i])

for i in range(q):
    t, l, r = map(int, input().split())
    t -= 1
    l -= 1
    ans = prefix[r] - prefix[l]
    l = bisect.bisect_left(idx[t], l)
    r = bisect.bisect_left(idx[t], r)
    ans -= (sum[t][r] - sum[t][l]) // 2
    print(ans)