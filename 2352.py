import sys
input = sys.stdin.readline

#nlogn
import bisect

def lis(li):
    lis = []
    for i in range(len(li)):
        #search binary search and append this index
        pos = bisect.bisect_left(lis, li[i])
        if pos < len(lis):
            lis[pos] = li[i]
        else:
            lis.append(li[i])
    #this is lis's index
    return lis

n = int(input())
li = list(map(int, input().split()))
print(lis(li))