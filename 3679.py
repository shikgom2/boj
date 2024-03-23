def ccw(x1, y1, x2, y2, x3, y3):
    c = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    return c > 0

def convex_hull(positions):
    convex = []
    for p3 in positions:
        while len(convex) >= 2:
            p1, p2 = convex[-2], convex[-1]
            if ccw(*p1, *p2, *p3):
                break
            convex.pop()
        convex.append(p3)

    return convex

N = int(input())
for _ in range(N):
    
    positions = []
    pos = list(map(int, input().split()))
    for i in range(1, len(pos), 2):
        positions.append([pos[i], pos[i+1]])

    positions = sorted(positions, key=lambda x: (x[0], x[1]))
    print(positions)

    low = convex_hull(positions)
    up = convex_hull(positions[::-1])

    convex = low[:-1] + up[:-1]
    top_left = min(convex, key=lambda p: (p[1], p[0]))

    top_left_index = convex.index(top_left)
    convex = convex[top_left_index:] + convex[:top_left_index]

    print(len(convex))
    for i in convex:
        print(i[0], -i[1])