n = int(input())
m = list(map(int, input().split()))

ans = []
for i in m:
    if i == 300:
        ans.append(1)
    elif i >= 275:
        ans.append(2)
    elif i >= 250:
        ans.append(3)
    else:
        ans.append(4)

print(*ans)