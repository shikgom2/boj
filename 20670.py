import sys
input = sys.stdin.readline

def ccw(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

def point_in_polygon(hull, point):

    s = 2
    e = len(hull) - 1
    while s < e:
        mid = (s + e) // 2
        if ccw(hull[0], hull[mid], point) < 0:
            e = mid
        else:
            s = mid + 1

    return ccw(hull[0], hull[s - 1], point) >= 0 and ccw(hull[s - 1], hull[s], point) >= 0 and ccw(hull[s], hull[0], point) >= 0


n, m, k = map(int, input().split())

li1 = list(map(int, input().split()))
li2 = list(map(int, input().split()))
li3 = list(map(int, input().split()))

poly1 = []
poly2 = []
points = []

off = 1000000000
for i in range(0, len(li1), 2):
    poly1.append((li1[i]+off, li1[i+1]+off))

for i in range(0, len(li2), 2):
    poly2.append((li2[i]+off, li2[i+1]+off))

for i in range(0, len(li3), 2):
    points.append((li3[i]+off, li3[i+1]+off))

ans = 0
for i in range(len(points)):
    if not point_in_polygon(poly1, points[i]) or point_in_polygon(poly2, points[i]):
        ans += 1

if(ans == 0):
    print("YES")
else:
    print(ans)