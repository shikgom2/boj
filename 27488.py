import sys
input = sys.stdin.readline 

t = int(input())
for _ in range(t):
    n = int(input())
    a, b, f, p = 0, 0, 0, 1

    while n:
        now = n % 10
        if now % 2 == 0:
            a += (now // 2) * p
            b += (now // 2) * p
        else:
            if f == 0:
                a += (now // 2 + 1) * p
                b += (now // 2) * p
            else:
                b += (now // 2 + 1) * p
                a += (now // 2) * p
            f ^= 1
        n //= 10
        p *= 10 
    print(a,b)