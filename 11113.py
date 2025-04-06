import sys
input = sys.stdin.readline
import math

n = int(input())
li = []
for _ in range(n):
    x, y = map(float, input().split())
    li.append((x, y))

m = int(input())
for _ in range(m):
    p = int(input())
    li2 = list(map(int, input().split()))
    ans = 0.0
    for i in range(p - 1):
        a = li2[i]
        b = li2[i + 1]
        dx = li[b][0] - li[a][0]
        dy = li[b][1] - li[a][1]
        ans += math.sqrt(dx * dx + dy * dy)
    print(round(ans))