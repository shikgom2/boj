import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    m = int(input())
    cur = 0
    mn = 0
    for _ in range(m):
        p1, p2 = map(int, input().split())
        cur += p1 - p2
        if cur < mn:
            mn = cur
    if mn < 0:
        print(-mn)
    else:
        print(0)
