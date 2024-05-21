n=int(input())
s = 10
while(n > s):
    t = n % s

    if(t >= s // 2):
        n += s
    n -= t
    s *= 10
print(n)