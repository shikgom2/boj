import sys
import heapq
input = sys.stdin.readline

n = int(input())
li = [0] + list(map(int, input().split()))
ans = [0] * (n + 1)
pq = []

for i in range(1, n + 1):
    a = li[i] - i
    heapq.heappush(pq, -a)
    heapq.heappush(pq, -a)
    heapq.heappop(pq)
    ans[i] = -pq[0] 

for i in range(n, 1, -1):
    if ans[i - 1] > ans[i]:
        ans[i - 1] = ans[i]

for i in range(1, n + 1):
    print(ans[i] + i)
