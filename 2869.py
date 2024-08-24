import sys
input = sys.stdin.readline

a,b,v = map(int, input().split())

if (v - a) % (a - b) == 0:
    print(f"{int((v - a) / (a - b) + 1)}")
else:
    print(f"{int((v - a) / (a - b) + 2)}")