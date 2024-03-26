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

def solve(x1, y1, x2, y2, x3, y3, x4, y4):
    A1 = y2 - y1
    B1 = x1 - x2
    C1 = A1 * x1 + B1 * y1
    A2 = y4 - y3
    B2 = x3 - x4
    C2 = A2 * x3 + B2 * y3

    determinant = A1 * B2 - A2 * B1
    if determinant == 0:
        return None

    x = (C1 * B2 - C2 * B1) / determinant
    y = (A1 * C2 - A2 * C1) / determinant
    return x, y

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

f1 = ccw(x1, y1, x2, y2, x3, y3)
f2 = ccw(x1, y1, x2, y2, x4, y4)
f3 = ccw(x3, y3, x4, y4, x1, y1)
f4 = ccw(x3, y3, x4, y4, x2, y2)

if f1 * f2 < 0 and f3 * f4 < 0:
    point = solve(x1, y1, x2, y2, x3, y3, x4, y4)
    print("1")
    print(f'{point[0]} {point[1]}')
else:
    if (f1 == 0 and on_segment(x1, y1, x2, y2, x3, y3)):
        print("1")
        print(f'{x3} {y3}')
    elif (f2 == 0 and on_segment(x1, y1, x2, y2, x4, y4)):
        print("1")
        print(f'{x4} {y4}')
    elif (f3 == 0 and on_segment(x3, y3, x4, y4, x1, y1)):
        print("1")
        print(f'{x1} {y1}')
    elif (f3 == 0 and on_segment(x3, y3, x4, y4, x1, y1)):
        print("1")
        print(f'{x1} {y1}')
    elif (f4 == 0 and on_segment(x3, y3, x4, y4, x2, y2)):
        print("1")
        print(f'{x2} {y2}')
    else:
        print("0")