import sys
input = sys.stdin.readline

def ccw(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

def point_in_polygon(hull, point):

    s = 2
    e = len(hull) - 1
    while s < e:
        mid = (s + e) >> 1
        if ccw(hull[0], hull[mid], point) < 0:
            e = mid
        else:
            s = mid + 1

    return ccw(hull[0], hull[s - 1], point) >= 0 and ccw(hull[s - 1], hull[s], point) >= 0 and ccw(hull[s], hull[0], point) >= 0

t = int(input())
for _ in range(t):
    li = list(map(int, input().split()))

    points = []
    off = 1000000
    points.append((li[0]+off, li[1]+off))
    points.append((li[2]+off, li[3]+off))
    points.append((li[4]+off, li[5]+off))
    points.append((li[6]+off, li[7]+off))

    if(point_in_polygon(points, (li[8]+off, li[9]+off))):
        print("Yes")
    else:
        print("No")