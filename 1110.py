n=int(input())
ans = 0
k = n
while(True):
    ans +=1
    tmp = (k//10)
    tmp1 = k%10
    if(n == tmp1*10+(tmp+tmp1)%10):
        print(ans)
        break
    else:
        k = tmp1*10+(tmp+tmp1)%10
        #print(k)