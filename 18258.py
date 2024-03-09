import sys
input = sys.stdin.readline
from collections import deque
li = deque()
N = int(input())

for _ in range(N):
    s = input().split()
    
    if(s[0] == 'push'):
        li.append(s[1])
    if(s[0] == 'pop'):
        if not(len(li)):
            print(-1)
        else:
            k = li.popleft()
            print(k)
    if(s[0] == 'size'):
        print(len(li))
    if(s[0] == 'empty'):
        if(len(li)):
            print(0)
        else:
            print(1)
    if(s[0] == 'front'):
        if not(len(li)):
            print(-1)
        else:
            k = li.popleft()
            print(k)
            li.appendleft(k)
    if(s[0] == 'back'):
        if not(len(li)):
            print(-1)
        else:
            k = li.pop()
            print(k)
            li.append(k)