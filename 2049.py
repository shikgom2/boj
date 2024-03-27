def ccw(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

def convex_hull(points):
    n = len(points)
    if n < 3:
        return points

    l = min(range(n), key=lambda i: points[i])
    hull = []

    p = l
    q = 0
    while True:
        hull.append(points[p])
        q = (p + 1) % n
        for i in range(n):
            if ccw(points[p], points[i], points[q]) == 2:
                q = i
        p = q
        if p == l:
            break

    return hull

def squared(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

def rotating_calipers(points):
    hull = convex_hull(points)
    n = len(hull)
    if n < 2:
        return None, None, 0
    if n == 2:
        return hull[0], hull[1], squared(hull[0], hull[1])

    k = 1
    while abs(ccw(hull[n-1], hull[0], hull[(k+1) % n])) > \
          abs(ccw(hull[n-1], hull[0], hull[k])):
        k += 1

    dist = 0
    pair = (None, None)
    for i in range(n):
        j = k
        while abs(ccw(hull[i], hull[(i+1) % n], hull[(j+1) % n])) > \
              abs(ccw(hull[i], hull[(i+1) % n], hull[j])):
            j = (j + 1) % n
        if squared(hull[i], hull[j]) > dist:
            dist = squared(hull[i], hull[j])
            pair = (hull[i], hull[j])
        k = j

    return pair[0], pair[1], dist

n=int(input())
points = []
for _ in range(n):
    i,j= map(int, input().split())
    points.append((i,j))
    
res = rotating_calipers(points)
print(res)