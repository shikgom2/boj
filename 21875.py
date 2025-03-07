import sys
input = sys.stdin.readline 

a = input()
b = input()

def f(c):
    return ord(c) - ord('a') + 1

col1, row1 = f(a[0]), int(a[1])
col2, row2 = f(b[0]), int(b[1])

dx = abs(col2 - col1)
dy = abs(row2 - row1)

x, y = min(dx, dy), max(dx, dy)
print(x, y)
