import sys
input = sys.stdin.readline

x, l, r = map(int, input().split())
ans = l
for i in range(l, r + 1):
    if abs(x - ans) > abs(x - i):
        ans = i

print(ans)