import sys
input = sys.stdin.readline

def ccw(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

def convex_hull(points):
    points = sorted(points)
    lower = []
    for p in points:
        while len(lower) >= 2 and ccw(lower[-2], lower[-1], p) < 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and ccw(upper[-2], upper[-1], p) < 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]

def rotating_calipers(points):
    def distance_sq(p1, p2):
        return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
    
    hull = convex_hull(points)
    n = len(hull)
    if n <= 1: return (0, 0), (0, 0)
    if n == 2: return hull[0], hull[1]

    k = 1
    max_dist = 0
    pair = (hull[0], hull[1])
    for i in range(n):
        while True:
            cur_dist = distance_sq(hull[i], hull[k])
            next_dist = distance_sq(hull[i], hull[(k + 1) % n])
            if cur_dist > max_dist:
                max_dist = cur_dist
                pair = (hull[i], hull[k])
            if cur_dist >= next_dist:
                break
            k = (k + 1) % n
    return pair

t = int(input())
for _ in range(t):
    n = int(input())
    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))

    hull = convex_hull(points)
    diameter_points = rotating_calipers(hull)

    print(len(hull))
    for p in hull:
        print(p[0], p[1])
    print(f"{diameter_points[0][0]} {diameter_points[0][1]} {diameter_points[1][0]} {diameter_points[1][1]}")