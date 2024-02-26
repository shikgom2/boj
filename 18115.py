import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.reverse()
d = deque()

cnt = 1
for i in arr:
    if(i == 1):
        d.appendleft(cnt)
    elif(i == 2):
        d.insert(1, cnt)    
    elif(i == 3):
        d.append(cnt)
    cnt += 1

print(*d)