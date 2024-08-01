n,k = map(int, input().split())

li = list(map(int, input().split()))
ans = []
for i in li:
    per = i * 100 // n
    if per <= 4:
        ans.append(1)
    elif per <= 11:
        ans.append(2)
    elif per <= 23:
        ans.append(3)
    elif per <= 40:
        ans.append(4)
    elif per <= 60:
        ans.append(5)
    elif per <= 77:
        ans.append(6)
    elif per <= 89:
        ans.append(7)
    elif per <= 96:
        ans.append(8)
    else:
        ans.append(9)

print(*ans)