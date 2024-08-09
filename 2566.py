import sys
input = sys.stdin.readline 

mi = 0
mj = 0
mval = 0

for i in range(9):
    li = list(map(int, input().split()))
    for k in range(len(li)):
        if(mval < li[k]):
            mi = i
            mj = k
            mval = li[k]
print(mval)
print(mi+1, mj+1)