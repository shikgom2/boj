li = list(map(int, input().split()))
li.sort()

if li[2] == li[0] + li[1]:
    print(1)
elif li[2] == li[0] * li[1]:
    print(2)
else:
    print(3)