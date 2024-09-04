import sys
input = sys.stdin.readline

def gcd(x,y):
    while(y):
        x,y = y,x%y
    return x
x,y = map(int, input().split())
tmp = gcd(x,y)

print(x + y - tmp)