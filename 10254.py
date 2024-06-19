import math

def CCW(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

def distance(a: list, b: list) -> int:
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

def convex_hull(graph):
    graph = sorted(set(graph))

    lower = []
    for i in graph:
        while len(lower) >= 2 and CCW(lower[-2], lower[-1], i) <= 0:
            lower.pop()
        lower.append(i)
        
    upper = []
    for i in reversed(graph):
        while len(upper) >= 2 and CCW(upper[-2], upper[-1], i) <= 0:
            upper.pop()
        upper.append(i)
    
    return lower[:-1] + upper[:-1]

def rotating_calipers(graph: list):
    if len(graph) == 2:
        return math.sqrt(distance(graph[0], graph[1])), (graph[0], graph[1])
    
    hull = convex_hull(graph)
    length = len(hull)

    result = 0
    farthest_points = (hull[0], hull[1])
    j = 1

    for i in range(length):
        next_i = (i + 1) % length

        while True:
            next_j = (j + 1) % length 

            d1 = CCW(hull[i], hull[next_i], hull[j])
            d2 = CCW(hull[i], hull[next_i], hull[next_j])

            if d1 < d2:
                j = next_j
            else:
                break

        dist_i_j = distance(hull[i], hull[j])
        dist_next_i_j = distance(hull[next_i], hull[j])
        
        if dist_i_j > result:
            result = dist_i_j
            farthest_points = (hull[i], hull[j])
        if dist_next_i_j > result:
            result = dist_next_i_j
            farthest_points = (hull[next_i], hull[j])
    
    return math.sqrt(result), farthest_points

t = int(input())
for _ in range(t):
    n = int(input())
    graph = []

    for _ in range(n):
        x, y = map(int, input().split())
        graph.append((x, y))

    graph = list(set(graph))

    ans, points = rotating_calipers(graph)
    #print(ans)
    print(points[0][0], points[0][1], points[1][0], points[1][1])