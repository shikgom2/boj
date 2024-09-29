import sys
input = sys.stdin.readline

def check(li, a):
    s = 0
    for i in range(len(li)):
        s += min(li[i], a)
    return s

n = int(input())
li = list(map(int, input().split()))
k = int(input())

li.sort()

left, right = 0, li[-1]
ans = 0

while left <= right:
    mid = (left + right) // 2

    if (check(li, mid) <= k):
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)