#공약수
def gcd(x,y):
    while(y):
        x,y = y,x%y
    return x
#공배수
def lcm(x,y):
    ans = (x*y)//gcd(x,y)
    return ans

t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    print(lcm(n,m))