import math
d = float(input())

ans = 0
ans = max(ans, math.sqrt(2) * d)

r = math.floor(d)
x = math.sqrt(d * d - r * r)

if x < 1 and d >= 1:
    ans = max(ans, r + 1)
print("{:.12f}".format(ans))