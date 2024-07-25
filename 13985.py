import sys
input = sys.stdin.readline

a, p, b, e, c = map(str, input().split())
if int(a) + int(b) == int(c):
    print("YES")
else:
    print("NO")