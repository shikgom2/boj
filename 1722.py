import sys
input = sys.stdin.readline
from itertools import permutations, combinations

n = int(input())
li = list(map(int, input().split()))

arr = []
for i in range(1, n+1):
    arr.append(i)

cur = 0
ans = []

for i in permutations(arr, n):
    a = i
    a = list(a)
    ans.append(a)

if(li[0] == 1): #kth
    print(*ans[li[1] - 1])
else: #permu
    del li[0]
    for i in range(len(ans)):
        if(ans[i] == li):
            print(i+1)