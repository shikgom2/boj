#공약수
def gcd(x,y):
    while(y):
        x,y = y,x%y
    return x
#공배수
def lcm(x,y):
    ans = (x*y)//gcd(x,y)
    return ans

i,j = map(int, input().split())

print(j-gcd(i,j))