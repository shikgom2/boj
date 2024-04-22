import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
li.sort()
x = int(input())

ans = 0
left = 0
right = len(li)-1
while(True):
    if(left >= right):
        break
    v = li[left] + li[right]
    if(v == x):
        ans += 1
    if(v < x):
        left += 1
    else:
        right -= 1
print(ans)