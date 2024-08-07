import sys
input = sys.stdin.readline

t = int(input())
for a in range(t):
    n = int(input())
    ans = 0
    c = True

    while n > 0:
        while n % 2 == 0:
            n //= 2
            ans += 1
            c = False
        n -= 1
        ans += 1
        if c:
            n //= 2 
    print(f'Case #{a+1}: {ans}')
