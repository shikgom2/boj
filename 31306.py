s = input()

ans1 = 0
ans2 = 0
li = ["a", "e", "i", "o", "u"]

for i in s:
    if i in li:
        ans1 += 1
        ans2 += 1
    if i == "y":
        ans2 += 1

print(ans1, ans2)