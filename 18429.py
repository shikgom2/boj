import sys
input = sys.stdin.readline 
import itertools

n,k = map(int ,input().split())
li = list(map(int, input().split()))

ncr = itertools.permutations(li, n)
ncr = list(ncr)
ans = 0
for i in range(len(ncr)):
    cur = 0
    flag = True
    for j in range(len(ncr[i])):
        cur += ncr[i][j]
        cur -= k

        if(cur < 0):
            flag = False
            break
    if(flag):
        ans += 1
print(ans)