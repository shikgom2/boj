import sys
input = sys.stdin.readline

n = int(input())
ans = 1
mod = 10007

if(n == 0):
    print(0)
else:
    while(n > 1):
        if(n == 4):
            n -= 4
            ans = ans * 4 % mod
        elif(n == 2):
            n -= 2
            ans = ans * 2 % mod
        else:
            n -= 3
            ans = ans * 3 % mod

    print(ans)