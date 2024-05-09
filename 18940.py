li = [0] * 205
li[1] = 1
li[2] = 1

for i in range(3, 205):
    check = [False] * 205
    check[li[i - 2]] = True
    check[li[i - 3]] = True
    for c in range(i - 2):
        tmp = li[i - c - 3] ^ li[c]
        check[tmp] = True
    for j in range(205):
        if not check[j]:
            li[i] = j
            break

t = int(input())
for _ in range(t):
    n = int(input())
    if n >= 100:
        n %= 34
        n += 34 * 3
    if li[n]:
        print("Yuto")
    else:
        print("Platina")