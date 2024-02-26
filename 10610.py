arr = list(input())
arr.sort(reverse=True)

s = 0
for i in arr:
    s += int(i)

if s % 3 == 0 and '0' in arr:
    for i in arr:
        print(i, end="")
else:
    print(-1)