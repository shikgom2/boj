l, r = map(int, input().split())

for i in range(l, r+1):
    check = [0] * 10
    tmp = i
    flag = True
    while(tmp):
        r = tmp % 10
        if(check[r]):
            flag = False
            break
        else:
            check[r] = True

        tmp = tmp // 10

    if(flag):
        print(i)
        exit()
print(-1)