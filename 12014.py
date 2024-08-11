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

t = int(input())
for a in range(t):
    n,k = map(int, input().split())
    li = list(map(int, input().split()))
    print(f"Case #{a+1}")
    if(lis(li) >= k):
        print(1)
    else:
        print(0)
