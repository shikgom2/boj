import sys
input = sys.stdin.readline
import heapq

n,a,b = map(int, input().split())

li1 = []
li2 = []
pq = []

for i in range(n):
    price_A, price_B = map(int, input().split())
    li1.append(price_A)
    li2.append(price_B)
    heapq.heappush(pq, (-(abs(price_A - price_B)), i))

ans = 0
while pq:
    _, idx = heapq.heappop(pq)
    if li1[idx] > li2[idx]:
        if b > 0:
            b -= 1
            ans += li2[idx]
        else:
            a -= 1
            ans += li1[idx]
    elif li1[idx] < li2[idx]:
        if a > 0:
            a -= 1
            ans += li1[idx]
        else:
            b -= 1
            ans += li2[idx]
    else:  # prices are the same
        ans += li1[idx]

print(ans)