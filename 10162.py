k = int(input())
a,b,c = 0,0,0

a = k // 300
k -= (300*a)

b = k // 60
k -= (60*b)

c = k // 10
k -= (10*c)

if(k != 0):
    print(-1)
else:
    print(f"{a} {b} {c}")