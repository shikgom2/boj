k = input()
ans = 0
for i in k:
    if i == "0":
        ans += 1

for i in k[::-1]:
    if i == "0":
        ans -= 1
    else:
        break

print(ans)