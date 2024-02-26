from collections import deque
import sys

d = deque()
arr = list(map(str, input()))

m = 'Z'

for a in arr:
    if(m >= a):
        m = a
        d.appendleft(a)
    else:
        d.append(a)
print(''.join(d))