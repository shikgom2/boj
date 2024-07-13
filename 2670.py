import sys
input = sys.stdin.readline
from itertools import combinations
from functools import reduce

n = int(input())
li = []
for _ in range(n):
    i = float(input())
    li.append(i)

ans = 0
for i in range(1, n):
    li[i] = max(li[i], li[i] * li[i-1])
print('%0.3f' % max(li))