import bisect
import sys
input = sys.stdin.readline
T = int(input())
a = int(input())
an = list(map(int, input().split()))
b = int(input())
bn = list(map(int, input().split()))

a_sum, b_sum = [], []
for i in range(a):
    for j in range(i+1, a+1):
        a_sum.append(sum(an[i:j]))
for i in range(b):
    for j in range(i + 1, b + 1):
        b_sum.append(sum(bn[i:j]))

a_sum.sort()
b_sum.sort()

ans = 0
for i in range(len(a_sum)):
    bmp = T - a_sum[i]
    left = bisect.bisect_left(b_sum, bmp)
    right = bisect.bisect_right(b_sum, bmp)
    ans += (right - left)
print(ans)