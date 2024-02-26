import math

original = []

def solve(center):
    tot = 0
    M = {}
    for i in range(n):
        if i == center:
            continue
        tx = original[i][0] - original[center][0]
        ty = original[i][1] - original[center][1]
        g = math.gcd(tx, ty)
        tx //= g
        ty //= g
        if g < 0:
            g = -g
        M[(tx, ty)] = M.get((tx, ty), 0) + 1
    
    for elem in M.items():
        x, y = elem[0]
        count = elem[1]
        if (-y, x) in M:
            tot += count * M[(-y, x)]
    return tot
n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    original.append((x, y))

sum = 0
for i in range(n):
    sum += solve(i)

print(sum)