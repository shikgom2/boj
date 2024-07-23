import sys
input = sys.stdin.readline

n = int(input())
ans = 0

if(n<0):
    ans = 32
elif(n == 0):
    ans = 1
else:
    while(n):
        n //= 2
        ans += 1

print(ans)