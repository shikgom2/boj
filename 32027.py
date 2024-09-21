import sys
input = sys.stdin.readline

n = int(input())
place = [False] * n  #check L R

left = []
right = []

for i in range(n):
    a, dir = input().split()
    a = int(a)
    if dir == "R":
        right.append(a)
        place[i] = True  # Marking as 'R'
    else:
        left.append(a)
        place[i] = False  # Marking as 'L'

if len(right) == 0 or len(left) == 0:
    print(n)
    exit()

left.sort()
right.sort()

#delete biggest cat
if(right[-1] < left[-1]):
    mxcat = left[-1]
    Md = False
    left.pop()
else:
    mxcat = right[-1]
    Md = True
    right.pop()

ans = 0

for i in range(n):
    if place[i] != Md:
        continue

    temp = [0] * n
    temp[i] = mxcat

    ridx = 0
    for j in range(i):
        if place[j]:
            temp[j] = right[ridx]
            ridx += 1

    lidx = 0
    for j in range(n-1, i, -1):
        if not place[j]:
            temp[j] = left[lidx]
            lidx += 1

    cnt = 1
    leftmax = 0
    for j in range(i):
        if not place[j]:
            while lidx < len(left) and left[lidx] <= leftmax:
                lidx += 1
            if lidx < len(left):
                cnt += 1
                temp[j] = left[lidx]
        leftmax = max(leftmax, temp[j])

    rightmax = 0
    for j in range(n-1, i, -1):
        if place[j]:
            while ridx < len(right) and right[ridx] <= rightmax:
                ridx += 1
            if ridx < len(right):
                cnt += 1
                temp[j] = right[ridx]
        rightmax = max(rightmax, temp[j])

    ans = max(ans, cnt)

print(ans)
