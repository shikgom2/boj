import sys
input = sys.stdin.readline

n = int(input())
points = []
for _ in range(n):
    x,y = map(float, input().split())
    points.append((x,y))
    
if n%2 == 1:
    print("NA")
else:
    mid = []
    for i in range(n):
        j = (i + (n // 2)) % n
        xi, yi = points[i]
        xj, yj = points[j]
        mid_x = (xi + xj) / 2.0
        mid_y = (yi + yj) / 2.0
        mid.append((mid_x, mid_y))
    Cx, Cy = mid[0]
    print(f"{Cx:.5f} {Cy:.5f}")