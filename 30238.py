import sys
input = sys.stdin.readline 

def solve():
    n = int(input())
    li = list(map(int, input().split()))

    #do behaiver
    #odd, add point and remove
    #greedy so, reverse....
    #if even and postive score, get twice
    ans = 0
    for i in range(len(li)):
        if(li[i] > 0):
            ans += li[i]

    if(n == 1 or li[0] >= 0 or li[1] < 0):
        print(ans)
    else:
        print(max(ans - li[1], ans + li[0]))

    
t =int(input())
for _ in range(t):
    solve()