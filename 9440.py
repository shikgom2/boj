while(True):
    li = list(map(int, input().split()))

    if(len(li) == 1 and li[0] == 0):
        break
    
    li.pop(0)
    li.sort()

    s1 = ""
    s2 = ""
    cnt = 0
    flag = True
    for i in range(len(li)):
        if(li[i] == 0):
            cnt += 1
        else:
            if(flag):
                flag = False
                s1 += str(li[i])
            else:
                s2 += str(li[i])
                flag = True

    for _ in range(cnt):
        if(len(s1) == len(s2)):
            s1 = s1[0] + '0' + s1[1:]
        else:
            s2 = s2[0] + '0' + s2[1:]

    print(int(s1)+int(s2))
