import sys
input = sys.stdin.readline
import heapq

n = int(input())
li = list(map(int, input().split()))
pq = []
ans = 0

for i in range(n):
    li[i] -= i
    heapq.heappush(pq, -li[i]) #maximum heapq

    if pq and -pq[0] > li[i]:
        ans += -pq[0] - li[i]
        heapq.heappop(pq)
        heapq.heappush(pq, -li[i])

print(ans)