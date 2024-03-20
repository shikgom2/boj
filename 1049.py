n,m = map(int, input().split())

package_min = 10**10
once_min = 10**10
for _ in range(m):
    a,b = map(int, input().split())
    package_min = min(package_min, a)
    once_min = min(once_min, b)

res = 0

if(package_min * (n//6) >= (once_min * n)):
    print((once_min * n))
else:
    if(n >= 6):
        res += package_min * (n//6)
        n = n%6 

    if(n > 0):
        if(package_min < (once_min * n)):
            res += package_min
        else:
            res += once_min * n

    print(res)