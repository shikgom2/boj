import sys 
n=int(input())
li=list(map(int,input().split()))
li.sort()
ans = 10**100
for i in range(n):
    ans = min(ans, li[i] + li[2 * n - i - 1])
print(ans)