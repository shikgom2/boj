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

t = int(input())
for _ in range(t):
    points = []
    li = list(map(int, input().split()))

    for i in range(1, li[0], 2):
        points.append((int(li[i]), int(li[i+1])))
    #points.append([int(li[0]), int(li[1])])

    print(len(convex_hull(points)))
    for p in convex_hull(points):
        print(p[0], p[1])