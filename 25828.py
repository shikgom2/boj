g, p, t = map(int, input().split())

g1 = g * p
g2 = g + t * p

if g1 < g2:
    print(1)
elif g1 > g2:
    print(2)
else:
    print(0)