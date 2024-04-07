i,j= map(int, input().split())
ans = j-i
if(ans==0):
    print(0)
else:
    a = 1
    while(True):
        if(a * a < ans):
            a += 1
        else:
            break 
    
    if(ans < (a * a) - a + 1):
        print(2 * a - 2)
    else:
        print(2 * a - 1)