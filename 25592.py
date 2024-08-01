import sys
input = sys.stdin.readline

n = int(input())

#1, 2, 3, 4, 5.....
#1, 3, 6, 10, 15...

cur = 1
while(n>=cur):
    n -= cur
    cur += 1
if(cur%2==0):
    print(0)
else:
    print(cur - n)