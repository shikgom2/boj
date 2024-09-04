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
    return len(lis), li

n = int(input())
li = list(map(int, input().split()))

print(lis(li))