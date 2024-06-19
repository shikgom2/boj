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

def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def solve(vertices):
    n = len(vertices)
    area = 0

    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[i][1] * vertices[j][0]
    
    return abs(area) / 2

n = int(input())
graph = []

for _ in range(n):
    li = list(map(str, input().split()))
    graph.append((int(li[0]), int(li[1])))

graph.sort()

convex = convex_hull(graph)
print(int(solve(convex)//50))