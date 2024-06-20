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

n = int(input())

poly = []
off = 10 ** 9

for _ in range(n):
    x, y = map(int, input().split())
    poly.append((x+off,y+off))

res = []
while(len(poly) != 0):
    hull = convex_hull(poly)
    #print(hull)    
    res.append(hull)
    hull_set = set(hull)
    poly = [point for point in poly if point not in hull_set]

#print(res)
m = int(input())
for _ in range(m):
    x, y = map(int, input().split())

    ans = 0
    for i in range(len(res)):
        if(point_in_polygon(res[i], (x+off,y+off))):
            ans += 1
    print(ans)