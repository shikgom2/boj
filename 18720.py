import sys
input = sys.stdin.readline
import heapq

t = int(input())
for _ in range(t):
    n, d = map(int, input().split())
    li = list(map(int, input().split()))
    pq = []
    ans = 0

    li.sort()
    
    for i in range(len(li)):
        li[i] = li[i] - i*d
    
    heapq.heapify(pq)

    x = [0] * n

    for i in range(n):
        heapq.heappush(pq, -li[i])
        heapq.heappush(pq, -li[i])
        x[i] = -heapq.heappop(pq) 

    for i in range(n - 2, -1, -1):
        x[i] = min(x[i], x[i + 1])

    ans = 0
    for i in range(n):
        ans += abs(li[i] - max(0, x[i]))

    print(ans)