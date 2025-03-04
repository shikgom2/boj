li = [int(input()) for _ in range(9)]
ss = sum(li)

target = ss - 100

found = False
for i in range(9):
    for j in range(i+1, 9):
        if li[i] + li[j] == target:
            num1, num2 = li[i], li[j]
            li.remove(num1)
            li.remove(num2)
            found = True
            break
    if found:
        break

li.sort()
for i in li:
    print(i)
