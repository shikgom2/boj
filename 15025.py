import sys
input = sys.stdin.readline
a, b = map(int, input().split())
if(a == b):
    if a == 0:
        print("Not a moose")
    else:
        print(f"Even {a+b}")
else:
    print(f"Odd {max([a, b])*2}")