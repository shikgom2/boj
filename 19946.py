import sys
input = sys.stdin.readline

n = int(input())
flag = False
ans = 1
while n != 1:
    if n % 2 == 0:
        n //= 2
        if flag: 
            ans += 1
    else:
        flag = True
        n = (n + 1) // 2
print(ans)