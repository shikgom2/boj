import sys
input = sys.stdin.readline
from collections import deque
li = deque()
N = int(input())

for _ in range(N):
    i = int(input())
    if(i == 0):
        li.popleft()
    else:
        li.appendleft(i)
print(sum(li))