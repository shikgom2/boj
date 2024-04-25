import math

def pow(a):
    return a * a

def min(a, b):
    return b if a > b else a

x1, y1, r1, x2, y2, r2 = map(float, input().split())

l = math.sqrt(pow(x2 - x1) + pow(y2 - y1))
ans = 0

if r1 + r2 <= l:
    ans = 0
elif r1 + r2 > l and abs(r1 - r2) < l:
    a = 2 * math.acos((pow(l) + pow(r1) - pow(r2)) / (2 * l * r1))
    b = 2 * math.acos((pow(l) + pow(r2) - pow(r1)) / (2 * l * r2))
    ans = (pow(r1) * (a - math.sin(a)) + pow(r2) * (b - math.sin(b))) / 2
else:
    ans = pow(min(r1, r2)) * math.pi

print(f"{ans:.3f}")