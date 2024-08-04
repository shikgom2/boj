import sys
input = sys.stdin.readline
import math

def dist(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def triangle_height(x1, y1, x2, y2, x3, y3):
    area = abs((x1 * y2) + (x2 * y3) + (x3 * y1) - (x1 * y3) - (x3 * y2) - (x2 * y1))
    return area / dist(x1, y1, x2, y2)

def inner(x1, y1, x2, y2):
    return x1 * x2 + y1 * y2

def perpendicular(x1, y1, x2, y2, x3, y3):
    L = inner(x2 - x1, y2 - y1, x3 - x1, y3 - y1)
    R = inner(x1 - x2, y1 - y2, x3 - x2, y3 - y2)
    return L >= 0 and R >= 0

n,m = map(int, input().split())
li = []
for _ in range(n):
    xs, ys, xe, ye = map(float, input().split())
    li.append((xs, ys, xe, ye))

ans = -1
for i in range(m):
    xs, ys, xe, ye = map(float, input().split())
    for j in range(n):
        x3 = li[j][0]
        y3 = li[j][1]
        x4 = li[j][2]
        y4 = li[j][3]

        tmp = dist(xs, ys, x3, y3)
        tmp = min(tmp , dist(xe, ye, x3, y3))
        tmp = min(tmp , dist(xs, ys, x4, y4))
        tmp = min(tmp , dist(xe, ye, x4, y4))

        if (perpendicular(xs, ys, xe, ye, x3, y3)):
              tmp = min(tmp, triangle_height(xs, ys, xe, ye, x3, y3))
        if (perpendicular(xs, ys, xe, ye, x4, y4)):
            tmp = min(tmp, triangle_height(xs, ys, xe, ye, x4, y4))
        if (perpendicular(x3, y3, x4, y4, xs, ys)):
            tmp = min(tmp, triangle_height(x3, y3, x4, y4, xs, ys))
        if (perpendicular(x3, y3, x4, y4, xe, ye)):
            tmp = min(tmp, triangle_height(x3, y3, x4, y4, xe, ye))

        if (ans == -1):
            ans = tmp
        else:
            ans = min(ans, tmp)
print(ans)