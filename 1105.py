i,j = list(map(str, input().split()))

li1 = list(str(i))
li2 = list(str(j))

if(len(li1) != len(li2)):
    print(0)
else:
    ans=0
    for i in range(len(li1)):
        if(li1[i] == li2[i]):
            if(li1[i] == '8'):
                ans+=1
        else:
            break
    print(ans)