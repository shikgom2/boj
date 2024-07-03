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

def rotating_calipers(graph):
    if len(graph) == 2:
        return distance(graph[0], graph[1])
    
    hull = convex_hull(graph)
    min_x = min(hull, key=lambda p: p[0])[0]
    max_x = max(hull, key=lambda p: p[0])[0]
    min_y = min(hull, key=lambda p: p[1])[1]
    max_y = max(hull, key=lambda p: p[1])[1]

    width = max_x - min_x
    height = max_y - min_y

    return 2 * (width + height)


while(True):    
    poly = []
    try:
        n = int(input())
    except Exception:
        break

    for _ in range(n):
        x,y = map(int, input().split())
        poly.append((x,y))

    print(rotating_calipers(poly))