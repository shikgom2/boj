import sys
input = sys.stdin.readline

def ccw(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

def area(point):
    n = len(point)
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += point[i][0] * point[j][1]
        area -= point[j][0] * point[i][1]
    return abs(area) / 2

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
tmp = []
for _ in range(n):
    li = list(map(str, input().split()))
    poly.append((int(li[0]), int(li[1])))
    tmp.append((int(li[0]), int(li[1])))


res = []
while(len(poly) > 2):
    hull = convex_hull(poly)
    #print(hull)    
    if(int(area(hull)) > 0):
        res.append(hull)
        
    hull_set = set(hull)
    poly = [point for point in poly if point not in hull_set]

#print(res)
for i in range(len(tmp)):
    x, y = tmp[i][0], tmp[i][1]
    flag = False
    for j in range(len(res)):
        for k in range(len(res[j])):
            if res[j][k] == (x, y):
                print(j+1, end=" ")
                flag = True
                break
        if flag:
            break
    if not flag:
        print(0, end=" ")