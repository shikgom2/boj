import sys
input = sys.stdin.readline
n,h = map(int, input().split())
li = list(map(int, input().split()))

if(sum(li) < h):
    print(-1)
else:
    ans = 0
    for i in range(n):
        ans += li[i]
        if(ans >= h):
            print(i+1)
            break