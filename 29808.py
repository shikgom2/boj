import sys
input = sys.stdin.readline

S = int(input().strip())
ZIP = 4763

if S % ZIP != 0:
    print(0)
    exit()
    
U = S // ZIP

s = set()

cases = [
    (508, 212, 1, 1),
    (508, 305, 1, 0),
    (108, 212, 0, 1),
    (108, 305, 0, 0),
]

for a, b, min_x, min_y in cases:
    for x in range(min_x, 201):
        rem = U - a * x
        if rem < 0:
            break
        if rem % b != 0:
            continue
        y = rem // b
        if y < min_y or y > 200:
            continue
        s.add((x, y))

ans = sorted(s)
print(len(ans))
for x, y in ans:
    print(x, y)
