a = input()
b = input()
for i in range(len(a)):
    if int(a[i]) > int(b[i]):
        print(a[i], end="")
    else:
        print(b[i], end="")
print()