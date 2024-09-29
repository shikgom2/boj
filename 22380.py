import sys
input = sys.stdin.readline

while(True):
    n,m = map(int, input().split())
    if(n == 0 and m == 0):
        break

    li = list(map(int, input().split()))
    want = m//n
    want = int(want)
    ans = 0
    for i in range(len(li)):
        ans += min(want, li[i])
    print(ans)