import sys
input = sys.stdin.readline

t = int(input())
cur= 1
for _ in range(t):
    x,y = map(int, input().split())
    if(x == cur):
        cur = y
    elif(y == cur):
        cur = x

print(cur)