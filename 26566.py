import math
n = int(input())
for _ in range(n):
    a1, p1 = map(int, input().split())
    r1, p2 = map(int, input().split())

    ans1 = a1 / p1
    ans2 = r1**2 * math.pi / p2

    if ans1 > ans2:
        print("Slice of pizza")
    else:
        print("Whole pizza")