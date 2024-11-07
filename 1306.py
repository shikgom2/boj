import sys
input = sys.stdin.readline
from collections import deque
        
n, m = map(int, input().split())
size = 2 * m - 1
li = list(map(int, input().split()))

dq = deque()

for i in range(n):
    while dq and li[dq[-1]] <= li[i]:
        dq.pop()
    dq.append(i)
    
    if dq[0] < i - size + 1:
        dq.popleft()

    if i >= size - 1:
        print(li[dq[0]], end=' ')