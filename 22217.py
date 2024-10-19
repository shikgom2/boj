import sys
input = sys.stdin.readline

n = input().strip()
n = int(n)

digits = []

while n != 0:
    r = n % 3
    if r == 0 or r == 1:
        c = r
        n = n // 3
    else:
        c = -1
        n = n // 3 + 1
    digits.append(c)

left = []
right = []

power = 1  # 3^0
for k, c in enumerate(digits):
    if c == -1:
        left.append(power)
    elif c == 1:
        right.append(power)
    power *= 3

left.sort()
right.sort()

print(len(left), *left)
print(len(right), *right)
