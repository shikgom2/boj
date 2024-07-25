import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    g, c, e = map(int, input().split())
    if g == 1:
        ans = 1
    elif g == 2:
        ans = 3
    elif g == 3:
        ans = 5
    if c > e:
        print(0)
    else:
        print((e - c) * ans)