def ccw(x1, y1, x2, y2, x3, y3):
    c = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    if c > 0:
        return 1
    elif c < 0:
        return -1
    else:
        return 0

def on_segment(x1, y1, x2, y2, x3, y3):
    if min(x1, x2) <= x3 <= max(x1, x2) and min(y1, y2) <= y3 <= max(y1, y2):
        return True
    return False

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

f1 = ccw(x1, y1, x2, y2, x3, y3)
f2 = ccw(x1, y1, x2, y2, x4, y4)
f3 = ccw(x3, y3, x4, y4, x1, y1)
f4 = ccw(x3, y3, x4, y4, x2, y2)

if f1 * f2 == 1 or f3 * f4 == 1:
    print(0)
elif f1 == 0 and f2 == 0:
    if x1 == x2:
        if max(y1, y2) < min(y3, y4) or max(y3, y4) < min(y1, y2):
            print(0)
        else:
            print(1)
    else:
        if max(x1, x2) < min(x3, x4) or max(x3, x4) < min(x1, x2):
            print(0)
        else:
            print(1)
else:
    print(1)