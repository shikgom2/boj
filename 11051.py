n, k = map(int, input().split())
res=1
for i in range(k):
    res=res*(n-i)
for i in range(1,k+1):
    res=res//i
print(res % 10007)