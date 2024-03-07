x, y, w, h = map(int, input().split())
li = [w - x, h - y, x, y]
print(min(li))