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


def find_dividing_points(points):
    n = len(points)
    hull = convex_hull(points)
    hull_set = set(hull)
    
    inside_points = [i + 1 for i in range(n) if (points[i][0], points[i][1]) not in hull_set]
    outside_points = [i + 1 for i in range(n) if (points[i][0], points[i][1]) in hull_set]
    
    if len(inside_points) > len(outside_points):
        return len(outside_points), outside_points
    else:
        return len(inside_points), inside_points

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

m, result = find_dividing_points(points)

print(m)
print(' '.join(map(str, result)))