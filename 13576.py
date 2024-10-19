import sys
input = sys.stdin.readline
from bisect import bisect_left

def z(s):
    n = len(s)
    l, r = -1, -1
    Z = [0] * n
    Z[0] = n
    
    for i in range(1, n):
        if i <= r:
            Z[i] = min(r - i + 1, Z[i - l])
        while i + Z[i] < n and s[Z[i]] == s[i + Z[i]]:
            Z[i] += 1
        if i + Z[i] - 1 > r:
            l, r = i, i + Z[i] - 1
    return Z


str = input().rstrip()
n = len(str)
z_li = z(str)
z_li[0] = n

arr = z_li[:]
arr.sort()

ans = []

print(z_li) 
for i in range(n - 1, -1, -1):
    if i + z_li[i] == n:
        count = len(arr) - bisect_left(arr, z_li[i])
        ans.append((z_li[i], count))

print(len(ans))
for i in range(len(ans)):
    print(ans[i][0], ans[i][1])        