import sys
input = sys.stdin.readline
import heapq

li = []
n = int(input())
for _ in range(n):
    s,e = map(int, input().split())
    li.append((s,e))

li.sort(key= lambda x : x[0])
pq = []

heapq.heappush(pq, li[0][1])

for i in range(1,n):
    if(li[i][0] >= pq[0]):
        heapq.heappop(pq)
    heapq.heappush(pq, li[i][1])
print(len(pq))