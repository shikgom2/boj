import sys
input = sys.stdin.readline

n = int(input())
li = []
for _ in range(n):
    x, y = map(int, input().split())
    li.append((x, y))

A2 = 0
Mx_num = 0
My_num = 0
Mx2_num = 0
My2_num = 0

for i in range(n):
    x0, y0 = li[i]
    x1, y1 = li[(i + 1) % n]
    cross = x0 * y1 - x1 * y0
    A2 += cross
    Mx_num += (x0 + x1) * cross
    My_num += (y0 + y1) * cross
    Mx2_num += (x0**2 + x0 * x1 + x1**2) * cross
    My2_num += (y0**2 + y0 * y1 + y1**2) * cross

A = A2 / 2.0

Mx = Mx_num / 6.0
My = My_num / 6.0
Mx2 = Mx2_num / 12.0
My2 = My2_num / 12.0

Ex = Mx / A
Ey = My / A
Ex2 = Mx2 / A
Ey2 = My2 / A

Varx = Ex2 - Ex * Ex
Vary = Ey2 - Ey * Ey

E_d2 = 2.0 * (Varx + Vary)

print("{0:.30f}".format(E_d2))