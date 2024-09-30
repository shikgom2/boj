import sys
import math

def position_M(t):
    return (ax + t * (bx - ax), ay + t * (by - ay))

def position_K(t):
    return (cx + t * (dx - cx), cy + t * (dy - cy))

def distance(t):
    Mx, My = position_M(t)
    Kx, Ky = position_K(t)
    return math.sqrt((Mx - Kx)**2 + (My - Ky)**2)

ax, ay, bx, by, cx, cy, dx, dy = map(int, input().split())

left = 0.0
right = 1.0

for _ in range(100):
    m1 = left + (right - left) / 3
    m2 = right - (right - left) / 3
    d1 = distance(m1)
    d2 = distance(m2)
    
    if d1 < d2:
        right = m2
    else:
        left = m1

t_min = (left + right) / 2
ans = distance(t_min)

print("{0:.20f}".format(ans))
