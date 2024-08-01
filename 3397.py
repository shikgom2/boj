import sys
input = sys.stdin.readline

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

t = int(input())
for _ in range(t):
    n = int(input())
    li = []
    for _ in range(n):
        s = int(input())
        li.append(s)
    if(n == 1):
        print("YES")
    else:
        li[1] //= gcd(li[0], li[1])
        for i in range(2, n):
            li[1] //= gcd(li[1], li[i])

        if(li[1] == 1):
            print("YES")
        else:
            print("NO")