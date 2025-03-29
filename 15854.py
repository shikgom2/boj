from bisect import bisect_right
import sys
inpuut = sys.stdin.readline

n, k, t = map(int, input().split())
li = list(map(int, input().split()))
li.sort()

if k == n:
    print(0)
    exit()
if t == 0:
    print(-1)
    exit()

pre = [0]*(n+1)
for i in range(n):
    pre[i+1] = pre[i] + li[i]

can = set()
can.add(0)
can.add(t-1)
for a in li:
    if a <= t-1:
        can.add(a)
can = list(can)
can.sort()

ans = float('inf')

for L in can:
    if L+1 > t:
        continue
    
    E = bisect_right(li, L)
    
    if E < k:
        r = k - E
        cost = (pre[E + r] - pre[E]) - r * L
    else:
        s = E - k
        cost = s * (L + 1) - (pre[E] - pre[E - s])
    
    ans = min(ans, cost)

print(ans if ans != float('inf') else -1)
