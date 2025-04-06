import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    li = [[0, 0] for _ in range(n)]
    for _ in range(m):
        a, b, p, q = map(int, input().split())
        li[a - 1][0] += p
        li[a - 1][1] += q
        li[b - 1][0] += q
        li[b - 1][1] += p
    
    mx = -1
    mn = 10**9
    for s, a in li:
        if s == 0 and a == 0:
            exp = 0.0
        else:
            exp = (s * s) / (s * s + a * a)
        tmp = int(exp * 1000)
        if tmp > mx:
            mx = tmp
        if tmp < mn:
            mn = tmp
    
    print(mx)
    print(mn)