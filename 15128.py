import sys
input = sys.stdin.readline

p1, q1, p2, q2 = map(int, input().split())
ans = p1 * p2 / q1 / q2 / 2
if ans == int(ans):
    print(1)
else:
    print(0)