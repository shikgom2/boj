n=int(input())
for _ in range(n):
    a = int(input())

    #min
    dp = [0, 0, 1, 7, 4, 2, 6, 8, 10, 18, 22]
    if a <= 10:
        print(dp[a], end=" ")
    else:
        ans = [8 for i in range((a+6)//7)]
        if a%7==1: 
            ans[0]=1
            ans[1]=0
        if a%7==2: 
            ans[0]=1
        if a%7==3: 
            ans[0]=2
            ans[1]=0
            ans[2]=0
        if a%7==4: 
            ans[0]=2
            ans[1]=0
        if a%7==5: 
            ans[0]=2
        if a%7==6: 
            ans[0]=6
        print(*ans, sep="", end=" ")
    #max
    if(a % 2) == 1:
        print(7, end="")
        a -= 3
    for i in range(a//2):
        print(1, end="")
    
    print("")