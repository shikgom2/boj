li = list(map(int,input()))
ans = 0

while(True):
    if(len(li) == 1):
        print(ans)

        if(li[0] == '3' or li[0] == '6' or li[0] == '9'):
            print("YES")
        else:
            print("NO")
        exit()

    li = list(map(int,str(sum(li))))
    ans += 1