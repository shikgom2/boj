import sys
input = sys.stdin.readline
import heapq

idx = 0

while(True):
    n, k1, k2 = map(int, input().split())
    if n == 0 and k1 == 0 and k2 == 0:
        break
    
    idx += 1
    smallest, largest = [], []
    
    li = list(map(int, input().split()))
    for d, item in enumerate(li, 1):
        heapq.heappush(smallest, (item, d))
        if len(smallest) > k1:
            heapq.heappop(smallest)
        heapq.heappush(largest, (-item, -d))
        if len(largest) > k2:
            heapq.heappop(largest)
    print(f"Case {idx}")

    sA = sorted([heapq.heappop(smallest)[1] for _ in range(k1)])
    print(' '.join(map(str, sA)))
    
    lA = sorted([-heapq.heappop(largest)[1] for _ in range(k2)], reverse=True)
    print(' '.join(map(str, lA)))