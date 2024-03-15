import sys
input = sys.stdin.readline
from collections import deque

N = int(input())

q = deque()

for _ in range(N):
    li = list(map(str, input().split()))

    if(li[0] == 'push'):
        q.append(li[1])
    elif(li[0] == 'pop'):
        if(len(q) == 0):
            print(-1)
        else:
            print(q.popleft())
    elif(li[0] == 'size'):
        print(len(q))
    elif(li[0] == 'empty'):
        if(len(q) == 0):
            print(1)
        else:
            print(0)
    elif(li[0] == 'front'):
        if(len(q) == 0):
            print(-1)
        else:
            print(q[0])
    elif(li[0] == 'back'):
        if(len(q) == 0):
            print(-1)
        else:
            print(q[len(q)-1])