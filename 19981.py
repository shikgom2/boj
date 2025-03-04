x = int(input().strip())

if x == 0:
    print(1)
    print(0)
    exit()

digits = []
while x:
    a = x % 2
    digits.append(a)
    x = (x - a) // -2

print(len(digits))
print(" ".join(map(str, digits)))
