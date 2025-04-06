import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    li = list(map(float, input().split()))
    total = sum(li)
    if total > 0:
        print("Right")
    elif total < 0:
        print("Left")
    else:
        print("Equilibrium")
