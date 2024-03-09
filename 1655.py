import heapq

minh, maxh = [], []

def add(n):
    heapq.heappush(maxh, -n)
    heapq.heappush(minh, -heapq.heappop(maxh))
    if len(minh) > len(maxh):
        heapq.heappush(maxh, -heapq.heappop(minh))

def median():
    if len(maxh) > len(minh):
        return -maxh[0]
    return (-maxh[0] + minh[0]) / 2

N = int(input())
for _ in range(N):
    i = int(input())
    add(i)
    print(median())