s = input()
ans = ""
for i in s:
    if ans == i:
        continue
    print(i, end="")
    ans = i
print()