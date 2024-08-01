n = int(input())
s = input()
ans = 0
for i in s:
    if i == "o":
        ans += 1
    else:
        ans += 2
print(ans)