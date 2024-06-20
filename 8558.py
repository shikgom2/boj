n = int(input())

if (n<= 1):
    print(1)
else:
    gop = 1
    for i in range(1,n+1):
        gop *= i
    gop %= 10
    print(gop)