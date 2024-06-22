import sys
input = sys.stdin.readline
import math

def ccw(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

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

def distance(target, p0, p1) :
    if p0[0] == p1[0] :
        return abs(target[0] - p0[0])
    if p0[1] == p1[1] :
        return abs(target[1] - p0[1])
    a, b = (p1[1] - p0[1]) / (p1[0] - p0[0]), -1
    c = -a * p0[0] + p0[1]
    return abs( a*target[0] + b*target[1] + c ) / (a**2 + b**2) ** 0.5

t = 0
while(True):
    t += 1
    n = int(input())
    if(n == 0):
        exit()

    points = []
    for _ in range(n):
        li = list(map(str, input().split()))
        points.append((int(li[0]), int(li[1])))

    hull = convex_hull(points)

    ans = 10 ** 10
    for i in range(len(hull)):
        k = (i + 1) % len(hull)
        tmp = 0
        for j in range(len(hull)) :
            tmp = max(tmp, distance(hull[j], hull[i], hull[k]))
        ans = min(ans, tmp)

    print('Case {:d}: {:0.02f}'.format(t, math.ceil(ans*100) / 100.0))