import sys
input = sys.stdin.readline

def ccw(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

def point_in_polygon(hull, point):
    if len(hull) < 3:
        return False

    s = 2
    e = len(hull) - 1
    while s < e:
        mid = (s + e) >> 1
        if ccw(hull[0], hull[mid], point) < 0:
            e = mid
        else:
            s = mid + 1
    if s == len(hull):
        s = len(hull) - 1

    return ccw(hull[0], hull[s - 1], point) >= 0 and ccw(hull[s - 1], hull[s], point) >= 0 and ccw(hull[s], hull[0], point) >= 0


def convex_hull(graph):
    graph = sorted(set(graph))

    lower = []
    for i in graph:
        while len(lower) >= 2 and ccw(lower[-2], lower[-1], i) <= 0:
            lower.pop()
        lower.append(i)
        
    upper = []
    for i in reversed(graph):
        while len(upper) >= 2 and ccw(upper[-2], upper[-1], i) <= 0:
            upper.pop()
        upper.append(i)
    
    return lower[:-1] + upper[:-1]

def polygon_centroid(points):
    n = len(points)
    if n < 3:  # 다각형이 아니면
        return None

    # 다각형의 넓이 계산
    area = 0
    cx = 0
    cy = 0

    for i in range(n):
        x0, y0 = points[i]
        x1, y1 = points[(i + 1) % n]
        a = x0 * y1 - x1 * y0
        area += a
        cx += (x0 + x1) * a
        cy += (y0 + y1) * a

    area *= 0.5

    if area == 0:
        # 넓이가 0인 경우, 유효하지 않은 다각형임
        raise ValueError("The area of the polygon is zero. The points might be collinear or invalid.")

    cx /= (6 * area)
    cy /= (6 * area)

    return (cx, cy)

n = int(input())
li = []
for _ in range(n):
    x,y = map(int, input().split())
    li.append((x,y))

cent = polygon_centroid(li)

li.append((0,0))
hull = convex_hull(li)
if len(hull) < 3:
    print("Yes")
elif(point_in_polygon(hull, cent)):
    print("No")
else:
    print("Yes")