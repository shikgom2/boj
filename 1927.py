import sys
import heapq
input = sys.stdin.readline
h = []
heapq.heapify(h)

N = int(input())
for _ in range(N):
    i = int(input())
    if(i == 0):
        if(len(h) == 0):
            print(0)
        else:
            val = heapq.heappop(h)
            print(val)
    else:   
         heapq.heappush(h, i)