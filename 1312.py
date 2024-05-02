a,b,n = map(int,input().split())
res = 0
for i in range(n+1):
    res = a//b
    a = a%b * 10
print(res)
