import heapq
import sys
input = sys.stdin.readline

n, t = map(int, input().split())
li = []

for _ in range(n):
    a, b = map(int, input().split())
    li.append((a,b+1))

li.sort(key=lambda k: (k[1], -k[0]))
pq = []
heapq.heapify(pq)
res = []
heapq.heapify(res)

day = 0
for p,d in sorted(li, key=lambda x : (x[1], -x[0])):
    heapq.heappush(res,p)
    day += 1
    if day > d:
        heapq.heappop(res)
        day -= 1 
print(sum(res))