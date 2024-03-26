i=int(input())

for _ in range(i):
    li = []
    while(True):
        a=int(input())
        if(a==0):
            break
        li.append(a)

    li.sort(reverse=True)
    res = 0
    pow = 1
    for l in li:
        res += 2 * (l ** pow)
        pow += 1

    if(res > 5 * 10 ** 6):
        print("Too expensive")
    else:
        print(res)