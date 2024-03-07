import math
n = 0
while True:
    n += 1
    d, r, t = map(float, input().split())
    if r == 0:
        break
    dis = d / 63360 * math.pi * r
    mph = dis / t * 3600
    print("Trip #%d: %.2f %.2f" % (n, dis, mph))