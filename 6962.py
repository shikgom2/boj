import math
import sys
input = sys.stdin.readline

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

def uclidan(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

def distance(points):
    d = 0
    l = len(points)
    
    for i in range(l):
        next_i = (i + 1) % l
        d  += uclidan(points[i], points[next_i])
    
    return d 

t = int(input())
for _ in range(t):
    n = int(input())
    points = []
    for _ in range(n):
        li = list(map(str, input().split()))
        points.append((int(li[0]), int(li[1])))

    poly = convex_hull(points)
    print(f"{distance(poly):.2f}")