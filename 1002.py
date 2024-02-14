import math

T = int(input())

for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    c1 = abs(r1 - r2)
    c2 = r1 + r2

    if d == 0:
        if c1 == 0:
            print("-1")
        else:                     
            print("0")
    else:        
        if c1 == d or c2 == d:
            print("1")
        elif (c1 < d and d < c2):
            print("2")
        else:
            print("0")