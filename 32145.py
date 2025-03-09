import sys
input = sys.stdin.readline

def cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

def convex_hull(points):
    points = sorted(points)
    if len(points) <= 1:
        return points
    flag = True
    for p in points:
        if cross(points[0], points[-1], p) != 0:
            flag = False
            break
    if flag:
        return points
    
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) < 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) < 0:
            upper.pop()
        upper.append(p)
    hull = lower[:-1] + upper[:-1]
    unique_hull = []
    seen = set()
    for p in hull:
        if p not in seen:
            unique_hull.append(p)
            seen.add(p)
    return unique_hull

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

if n <= 2:
    print(n-1)
    exit()

hull = convex_hull(points)

if len(hull) == n:
    flag = True
    for p in points:
        if cross(points[0], points[-1], p) != 0:
            flag = False
            break
    if flag:
        print(n-1)
    else:
        print(3*n - 3 - len(hull))
else:
    print(3*n - 3 - len(hull))
