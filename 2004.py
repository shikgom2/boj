import math
def solve(num, x) :
    t = x
    sum = 0
    while t<= 10**9*2 :
        sum += num//t
        t *= x
    return sum

n,m = map(int, input().split())

if m < 0 or m>n :
    print(0)
    
else :
    res = solve(n,5) - solve(m,5) - solve(n-m,5)
    res1 = solve(n,2) - solve(m,2) - solve(n-m,2)
    print(min(res, res1))