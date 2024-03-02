import heapq

h1 = []
h2 = []
heapq.heapify(h1)
heapq.heapify(h1)

for _ in range(4):
    i = int(input())
    heapq.heappush(h1, i)
for _ in range(2):
    i = int(input())
    heapq.heappush(h2, i)
heapq.heappop(h1)
heapq.heappop(h2)

print(sum(h1) + sum(h2))