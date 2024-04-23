import sys
input = sys.stdin.readline

def solve():
    n,m = map(int, input().split())
    li = list(map(int, input().split()))
    li.sort()

    ans = 0
    left = 0
    right = len(li)-1
    val = 10**10
    while(True):
        if(left >= right):
            break
        v = li[left] + li[right]
        
        #1.
        if(abs(m - val) > abs(m - v)):
            val = v
            ans = 1
        #2.
        elif(abs(m-v) == abs(m-val)):
            ans += 1

        if(v < m):
            left += 1
        else:
            right -= 1
    print(ans)

t = int(input())
for _ in range(t):
    solve()