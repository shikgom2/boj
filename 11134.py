import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a,b=map(int, input().split())
    if(a%b):
        print(a//b + 1)
    else:
        print(a//b)