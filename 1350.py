n = int(input())
li = list(map(int, input().split()))
c = int(input())

total = 0
for size in li:
    if size > 0:
        clusters = (size + c - 1) // c
        total += clusters * c

print(total)
