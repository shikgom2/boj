import sys
input = sys.stdin.readline
from collections import deque
li = deque()
N = int(input())

for _ in range(N):
    s = input().split()
    
    if(s[0] == '1'):
        li.append(s[1])
    elif(s[0] == '2'):
        if(len(li) == 0):
            print(-1)
        else:
            print(li.pop())
    elif(s[0] == '3'):
        print(len(li))
    elif(s[0] == '4'):
        if(len(li)):
            print(0)
        else:
            print(1)
    elif(s[0] == '5'):
        if(len(li) == 0):
            print(-1)
        else:
            k = li.pop()
            print(k)
            li.append(k)