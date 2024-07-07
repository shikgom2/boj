import sys
input = sys.stdin.readline

#공약수
def gcd(x,y):
    while(y):
        x,y = y,x%y
    return x
#공배수
def lcm(x,y):
    ans = (x*y)//gcd(x,y)
    return ans

li1 = list(map(int, input().split()))
li2 = list(map(int, input().split()))

k = lcm(li1[1], li2[1])

li1[0] = li1[0] * (k // li1[1])
li1[1] = li1[1] * (k // li1[1])
li2[0] = li2[0] * (k // li2[1])
li2[1] = li2[1] * (k // li2[1])

ans1 = li1[0] + li2[0]
ans2 = li1[1]

k = gcd(ans1, ans2)
ans1 //= k
ans2 //= k

print(ans1, ans2)