import sys
input = sys.stdin.readline
import heapq

t = int(input())

for _ in range(t):
    n, d = map(int, input().split())
    c = list(map(int, input().split()))

    min_heap = []
    max_heap = []
    total_time = 0

    for ci in c:
        heapq.heappush(min_heap, ci)
        heapq.heappush(max_heap, -ci)

        min_needed = heapq.heappop(min_heap)
        max_needed = -heapq.heappop(max_heap)

        if max_needed - min_needed < d:
            if min_needed < ci:
                total_time += ci - min_needed
                heapq.heappush(min_heap, ci)
                heapq.heappush(max_heap, -(min_needed + d))
            else:
                total_time += max_needed - ci
                heapq.heappush(min_heap, max_needed - d)
                heapq.heappush(max_heap, -ci)
        else:
            heapq.heappush(min_heap, min_needed)
            heapq.heappush(max_heap, -max_needed)

        print(total_time)