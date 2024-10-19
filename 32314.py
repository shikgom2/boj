import sys
input= sys.stdin.readline

n = int(input())
w,v = map(int, input().split())
if(w/n >= v):
    print(1)
else:
    print(0)