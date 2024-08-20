import sys
input = sys.stdin.readline
from collections import Counter

n,k = map(int, input().split())
li = []
for _ in range(n):
    a=int(input())
    li.append(a)

li.sort()

li[n-k:n] = sorted(li[n-k:n], reverse=True)

if li[n-k-1] > k:
    print(-1)
    exit()

for i in range(n-1, n-k-1, -1):
    if li[i] <= n-i-1:
        print(-1)
        exit()

print(" ".join(map(str, li)))