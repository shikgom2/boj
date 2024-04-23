import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
li.sort()

ans = 10**10
left = 0
right = len(li)-1
while(True):
    if(left >= right):
        break
    v = li[left] + li[right]
    if(abs(v) < abs(ans)):
        ans = v
    if(v < 0):
        left += 1
    else:
        right -= 1
print(ans)