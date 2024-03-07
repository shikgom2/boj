import sys
input = sys.stdin.readline
import heapq
import collections

N = int(input())
x = list(map(int, input().split()))
setX = list(set(x))
h = []
for i in setX:
    heapq.heappush(h, i)
ord = collections.defaultdict(int)
for i in range(len(h)):
    ord[heapq.heappop(h)] = i

for a in x:
    print(ord[a], end=" ")