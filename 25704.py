n = int(input())
p = int(input())

li = [p]

if n >= 5:
    li.append(max(p - 500, 0))
if n >= 10:
    li.append(max(p * 9 // 10, 0))
if n >= 15:
    li.append(max(p - 2000, 0))
if n >= 20:
    li.append(max(p * 3 // 4, 0))

print(min(li))