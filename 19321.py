import sys
from bisect import bisect_left
input = sys.stdin.readline

def bs(a, x):
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid][0] < x[0]:
            lo = mid + 1
        else:
            hi = mid
    return lo

n = int(input())
li = list(map(int, input().split()))

seq = []
for i in range(n):
    seq.append((li[i], i))

seq.sort()
ret = list(seq)

val = n

for i in range(n, 0, -1):
    x = (i, -1)
    idx = bs(seq, x)
    if idx == n:
        continue
    else:
        for j in range(idx, n):
            ret[j] = (val, ret[j][1])
            val -= 1
            if j == n - 1 or seq[j][0] != seq[j + 1][0]:
                break

ret.sort(key=lambda x: x[1])
print(' '.join(str(x[0]) for x in ret))