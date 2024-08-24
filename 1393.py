import sys
input = sys.stdin.readline
import math

def d(x1, y1, x2, y2):
    d= math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return d

def gcd(x,y):
    while(y):
        x,y = y,x%y
    return x
    
xs, ys = map(int, input().split())
xe, ye, dx, dy = map(int, input().split())

if(dx == 0 and dy == 0):
    print(xs, ys)
    exit()
    
g = gcd(dx, dy)
dx = dx // g
dy = dy // g

curx, cury = xe, ye
while d(curx, cury, xs, ys) > d(curx + dx, cury + dy, xs, ys):
    curx += dx
    cury += dy
    
print(curx, cury)
