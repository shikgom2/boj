import heapq
import sys
input = sys.stdin.readline

N = int(input())
q = []
heapq.heapify(q)

for _ in range(N):
    tmp = int(input())
    heapq.heappush(q, tmp)

cnt = 0
sum = 0
for _ in range(N-1):
    tmp1 = heapq.heappop(q)
    tmp2 = heapq.heappop(q)
    sum = sum + tmp1 + tmp2
    heapq.heappush(q, (tmp1 + tmp2))

print(sum)
