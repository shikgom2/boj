import sys
input = sys.stdin.readline
from collections import deque

d = [[-1 for _ in range(10)] for _ in range(10)]

def check(n1, n2):
    if d[n1][n2] != -1:
        return d[n1][n2]
    if n1 == 0 and n2 == 0:
        d[n1][n2] = 1
        return True
    if n2 == 0 or n2 == 1:
        d[n1][n2] = 1
        return True
    
    for x in range(1, 3):
        if x == 1 and n1 == 0:
            continue
        if x == 2 and n2 == 0:
            continue
        for a1 in range(0, n1 - (x == 1) + 1):
            for a2 in range(0, n2 - (x == 2) + 1):
                b1 = n1 - a1 - (x == 1)
                b2 = n2 - a2 - (x == 2)
                assert b1 >= 0
                assert b2 >= 0
                if abs(a1 + 2 * a2 - b1 - 2 * b2) <= 1:
                    if check(a1, a2) and check(b1, b2):
                        d[n1][n2] = 1
                        return True
    d[n1][n2] = 0
    return False

def can(n1, n2):
    nn2 = n2
    n2 |= n2 >> 1
    n2 |= n2 >> 2
    n2 |= n2 >> 4
    n2 |= n2 >> 8
    n2 |= n2 >> 16
    return n2 - nn2 <= n1

# Tree structure
nv = 1
l = [0] * 500001
r = [0] * 500001
z = [0] * 500001

def build(n1, n2):
    global nv
    if n1 + n2 == 0:
        return 0
    
    v = nv
    nv += 1

    for x in range(1, 3):
        if x == 1 and n1 == 0:
            continue
        if x == 2 and n2 == 0:
            continue
        r1 = n1 - (x == 1)
        r2 = n2 - (x == 2)
        
        s = (n1 + 2 * n2 - x) // 2
        for a2 in range(0, r2 + 1):
            rem = s - a2 * 2
            for a1 in range(rem - 2, rem + 2 + 1):
                if a1 >= 0 and a1 <= r1:
                    b1 = r1 - a1
                    b2 = r2 - a2
                    assert b1 >= 0 and b1 <= r1
                    assert b2 >= 0 and b2 <= r2
                    if abs((a1 + 2 * a2) - (b1 + 2 * b2)) <= 1:
                        if can(a1, a2) and can(b1, b2):
                            z[v] = x
                            l[v] = build(a1, a2)
                            r[v] = build(b1, b2)
                            return v
    assert False

a, b = map(int, input().split())
if not can(a, b):
    print("-1")
    exit()

build(a, b)
for i in range(1, a + b + 1):
    print(f"{z[i]} {l[i]} {r[i]}")
