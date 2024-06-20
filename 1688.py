import sys
input = sys.stdin.readline 

def is_point_on_line_segment(p, p1, p2):
    x, y = p
    x1, y1 = p1
    x2, y2 = p2

    if min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2):
        if x1 == x2:
            return x == x1
        if y1 == y2:
            return y == y1

        return (x - x1) * (y2 - y1) == (y - y1) * (x2 - x1)
    
    return False

def ray_cast_algorithm(polygon, point):
    x, y = point
    n = len(polygon)
    inside = False

    p1x, p1y = polygon[0]
    for i in range(n + 1):
        p2x, p2y = polygon[i % n]
        
        if is_point_on_line_segment(point, (p1x, p1y), (p2x, p2y)):
            return True

        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y

    return inside

n = int(input())
points = []
for _ in range(n):
    li = list(map(str, input().split()))
    points.append((int(li[0]), int(li[1])))

for _ in range(3):
    x, y = map(int, input().split())
    if(ray_cast_algorithm(points, (x,y))):
        print(1)
    else:
        print(0)