import sys
input = sys.stdin.readline

def check(a1, a2, b1, b2):
    # Negative if a1/a2 < b1/b2
    return a1 * b2 - a2 * b1

b,c,d = map(int, input().split())
a1, a2 = map(int, input().split())
e1, e2 = map(int, input().split())

ans = 0
for i in range(1, 1000001):
    if check(a1, a2, i, c) >= 0:
        continue
    if check(i, c, e1, e2) >= 0:
        break
    ans += ((e1 * d - 1) // e2 - (i * d) // c) * ((b * i - 1) // c - (a1 * b) // a2)
print(ans)