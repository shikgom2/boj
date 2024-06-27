import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
li = deque()

for _ in range(n):
    x, y = map(int, input().split())
    li.append(y)
