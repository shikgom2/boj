a, b= map(int, input().split())

if(b == 0 or a <= 1):
    print(0)
    exit()
else:
    ans = 3
    a -= 2
    b -= 1

    while(True):
        if(a == 0 or b == 0):
            break 

        a -= 1
        b -= 1
        ans += 2
    
    print(ans)