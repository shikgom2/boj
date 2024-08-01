h, w = map(int, input().split())
r = 0
b = 0
for _ in range(h):
    s = input()
    for i in s:
        if i == "0":
            r += 1
        else:
            b += 1
print(min(r, b))