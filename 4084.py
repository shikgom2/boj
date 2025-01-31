def solve(a, b, c, d):
    steps = 0
    while not (a == b == c == d):
        new_a = abs(a - b)
        new_b = abs(b - c)
        new_c = abs(c - d)
        new_d = abs(d - a)
        a, b, c, d = new_a, new_b, new_c, new_d
        steps += 1
        if steps > 1000:
            break
    return steps

while(True):
    a, b, c, d = map(int, input().split())
    if a == 0 and b == 0 and c == 0 and d == 0:
        break
    steps = solve(a, b, c, d)
    print(steps)
