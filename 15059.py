import sys
input = sys.stdin.readline

a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())
ans = 0
if a1 < a2:
    ans += a2 - a1
if b1 < b2:
    ans += b2 - b1
if c1 < c2:
    ans += c2 - c1
print(ans)