import sys
input = sys.stdin.readline
import math

def solve(p):
    hif = int(math.sqrt(p))
    below = hif * (hif + 1) // 2
    r = p + p * (p + 1) // 2 - below
    f = 2
    while f * f <= p:
        r += f * (p // f)
        if f * f != p:
            cnt = p // f
            r += cnt * (cnt + 1) // 2 - below
        f += 1
    return r

a,b=map(int, input().split())
print(solve(b) - solve(a - 1))