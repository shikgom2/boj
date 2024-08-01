
while(True):
    n = int(input())
    if(n == 0):
        break
    li = list(map(int, input().split()))
    ans = 0
    for i in range(2, n):
        ans = max(ans, li[i-2] + li[i-1] + li[i])
    print(ans)