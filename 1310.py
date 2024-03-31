import sys
input = sys.stdin.readline

def ccw(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

def dist(A, B):
    dx = A[0] - B[0]
    dy = A[1] - B[1]
    return dx*dx + dy*dy

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

n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

hull = convex_hull(points)

r = 0
ans = 0
n = len(hull)
for i in range(n):
    while ccw(hull[i], hull[(i + 1) % n], (hull[(i + 1) % n][0] + hull[(r + 1) % n][0] - hull[r % n][0], hull[(i + 1) % n][1] + hull[(r + 1) % n][1] - hull[r % n][1])) >= 0:
        ans = max(ans, dist(hull[i], hull[r % n]))
        r += 1
        if r >= n * 2:
            break
    ans = max(ans, dist(hull[i], hull[r % n]))

print(ans)
