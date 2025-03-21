import sys, math
input = sys.stdin.readline

def query(h):
    if seg_sum[1] < h:
        return -1
    ans = 0
    i = 1
    while i < n:
        left = 2 * i
        if seg_sum[left] >= h:
            i = left
        else:
            ans += seg_count[left]
            h -= seg_sum[left]
            i = left + 1
    pos = i - n
    val = vals[pos]
    needed = (h + val - 1) // val
    ans += needed
    return ans

def update(pos, val):
    i = n + pos
    seg_count[i] += 1
    seg_sum[i] += val
    i //= 2
    while i:
        seg_count[i] = seg_count[2 * i] + seg_count[2 * i + 1]
        seg_sum[i] = seg_sum[2 * i] + seg_sum[2 * i + 1]
        i //= 2
        
h = int(input())
n, q = map(int, input().split())
li = list(map(int, input().split()))
querys = [int(input()) for _ in range(q)]

all_cards = li + querys
vals = sorted(set(all_cards), reverse=True)
M = len(vals)
comp = {v: i for i, v in enumerate(vals)}

freq = [0] * len(vals)
for v in li:
    freq[comp[v]] += 1

n = 1
while n < M:
    n *= 2

seg_count = [0] * (2 * n)
seg_sum = [0] * (2 * n)

for i in range(M):
    seg_count[n + i] = freq[i]
    seg_sum[n + i] = freq[i] * vals[i]

for i in range(n - 1, 0, -1):
    seg_count[i] = seg_count[2 * i] + seg_count[2 * i + 1]
    seg_sum[i] = seg_sum[2 * i] + seg_sum[2 * i + 1]

ans = query(h)

print(ans)

for x in querys:
    pos = comp[x]
    update(pos, x)
    ans = query(h)
    print(ans)