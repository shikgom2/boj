import sys
import heapq

input = sys.stdin.readline

n = int(input())
v = list(map(int, input().split()))
k = int(input())

pq = [(-val, i, 1) for i, val in enumerate(v)] 
heapq.heapify(pq)

print(pq)

mn = min(v)
res = -pq[0][0] - mn

for _ in range(k):
    val, idx, cnt = heapq.heappop(pq)
    val = -(v[idx] / (cnt + 1))
    cnt += 1
    heapq.heappush(pq, (val, idx, cnt))
    mn = min(mn, -val)
    res = min(res, -pq[0][0] - mn)
print(f"{res:.20f}")