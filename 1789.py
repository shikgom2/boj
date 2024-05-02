n=int(input())
k = 1
while(True):
    n -= k
    if(n == 0):
        print(k)
        break
    elif(n < 0):
        print(k-1)
        break

    k+=1