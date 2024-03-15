x = int(input())
i, j = 0, 0
while x > j:
    i += 1
    j += i

if i % 2 == 0:
    a = i - (j - x)
    b = (j - x) + 1
else:
    a = (j - x) + 1
    b = i - (j - x)

print(f'{a}/{b}')