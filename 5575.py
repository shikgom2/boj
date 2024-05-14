for _ in range(3):
    a,b,c,d,e,f = map(int, input().split())

    a = a * 60 * 60
    b = b * 60
    
    d = d * 60 * 60
    e = e * 60

    ans1 = a+b+c
    ans2 = d+e+f

    ans = ans2 - ans1
    print(ans//3600, (ans%3600)//60, (ans%60))