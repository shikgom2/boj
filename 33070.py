from bisect import bisect_left
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
li = list(map(int, input().split()))

off = [0]*(N+1)
for i in range(N):
    off[i+1] = off[i] + (1 if li[i] == 0 else 0)

cnt = 0
for i in range(N):
    if li[i] == 1:
        
        g = off[i]
        lo, hi = g, g + cnt
        idx = bisect_left(A, lo)
        if idx < len(A) and A[idx] <= hi:
            cnt += 1

ans = off[N] + cnt
print(N - ans)
