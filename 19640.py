import heapq
from collections import deque

n, m, k = map(int, input().split())

li = [deque() for _ in range(m)]
pq = []
me = None

for i in range(n):
    d, h = map(int, input().split())
    emp = (i, d, h, i % m)
    li[i % m].append(emp)
    if i == k:
        me = emp

for i in range(m):
    if li[i]:
        heapq.heappush(pq, (-li[i][0][1], -li[i][0][2], li[i][0][3], li[i][0]))

ans = 0
while pq:
    _, _, _, front = heapq.heappop(pq)
    
    if front == me:
        break
    
    li[front[3]].popleft()
    if li[front[3]]:
        heapq.heappush(pq, (-li[front[3]][0][1], -li[front[3]][0][2], li[front[3]][0][3], li[front[3]][0]))
    
    ans += 1
print(ans)