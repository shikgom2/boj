while(True):
    n=int(input())
    if(n==0):
        break
    li = list(map(int, input().split()))
    res = 0
    ans = 0
    for i in li:
        res = res ^ i
    for i in li:
        if(i ^ res) < i:
           ans += 1 
    print(ans)