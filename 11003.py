from collections import deque
import heapq
import sys
input = sys.stdin.readline

N, L = map(int, input().split())
arr = list(map(int, input().split()))

d = deque()

for k in arr:
    d.append(k)
    #print(d)

    hq = list(d)
    heapq.heapify(hq)
    val = heapq.heappop(hq)
    print(val, end=" ")

    if(len(d) == L):
        d.popleft()
        #print(d)