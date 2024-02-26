N = int(input())
for _ in range(N):
    k = int(input())
    a,b,c,d = 0,0,0,0
    
    a = k // 25
    k -= (25*a)

    b = k // 10
    k -= (10*b)

    c = k // 5
    k -= (5*c)
    
    print(f"{a} {b} {c} {k}")