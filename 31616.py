n = int(input())
s = input()

c = s[0]
flag = True
for i in s:
    if i != c:
        flag = False
        break
if flag:
    print("Yes")
else:
    print("No")