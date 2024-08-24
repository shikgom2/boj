import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):

    n,m = map(int,input().split())
    
    li = list(map(int,input().split()))
    order = [x for x in range(len(li))]
    
    ans = 0
    while True:
        if li[0] >= max(li):
            ans += 1
            if order[0] == m:
                break
            else:
                li = li[1:]
                order = order[1:]
        else:
            li = li[1:] + li[:1]
            order = order[1:] + order[:1]
    print(ans)