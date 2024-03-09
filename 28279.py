import sys
input = sys.stdin.readline
from collections import deque


N = int(input())
li = deque()

def checklen(d):
    if(len(d) == 0):
        print(-1)
        return False
    else:
        return True

for _ in range(N):
    s = list(map(int, input().split()))

    if(s[0] == 1):
        li.appendleft(s[1])
    if(s[0] == 2):
        li.append(s[1])
    if(s[0] == 3):
        if(checklen(li)):
            print(li.popleft())
    if(s[0] == 4):
        if(checklen(li)):
            print(li.pop())
    if(s[0] == 5):
        print(len(li))
    if(s[0] == 6):
        if(len(li) == 0):
            print(1)
        else:
            print(0)
    if(s[0] == 7):
        if(checklen(li)):
            k = li.popleft()
            print(k)
            li.appendleft(k)
    if(s[0] == 8):
        if(checklen(li)):
            k = li.pop()
            print(k)
            li.append(k)