import sys
input = sys.stdin.readline
import bisect

def lis(li):
    lis = []
    for x in li:
        pos = bisect.bisect_left(lis, x)
        if pos < len(lis):
            lis[pos] = x
        else:
            lis.append(x)
    return len(lis)

n = int(input())
li = list(map(int, input().split()))

#n log n, tracking to o(n)?
ans = lis(li)

if(n-ans <= 3):
    print("YES")
    print(n-ans)
else:
    print("NO")