n = int(input())
count = 0
for a in range(0, 100):
    b = n - a
    if 0 <= b <= 99:
        count += 1
print(count)
