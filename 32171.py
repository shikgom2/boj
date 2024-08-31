import sys
input = sys.stdin.readline

n = int(input())

minx = 10**10
miny = 10**10
maxx = -10**10
maxy = -10**10

for _ in range(n):
    a,b,c,d = map(int, input().split())
    minx = min(a,c,minx)
    miny = min(b,d,miny)
    maxx = max(a,c,maxx)
    maxy = max(d,b,maxy)

    print(2 * (maxx-minx) + 2 * (maxy-miny))