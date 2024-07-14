li = []
for _ in range(6):
    s = input()
    li.append(s)

ans = li.count('W')
if ans >= 5:
    print(1)
elif ans >= 3:
    print(2)
elif ans >= 1:
    print(3)
else:
    print(-1)