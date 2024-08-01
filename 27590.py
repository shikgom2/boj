d1, y1 = map(int, input().split())
d2, y2 = map(int, input().split())

sun = y1 - d1
moon = y2 - d2

while sun != moon:
    if sun < moon:
        sun += y1
    else:
        moon += y2
print(sun)