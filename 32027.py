import sys
input = sys.stdin.readline

n = int(input())
place = [False] * n  #check L R

left = []
right = []

for i in range(n):
    a, dir = input().split()
    a = int(a)
    if(dir == "R"):
        right.append(a)
        place[i] = "R"
    else:
        left.append(a)
        place[i] = "L"

if len(right) == 0 or len(left) == 0:
    print(n)
    exit()

left.sort()
right.sort()

#delete biggest cat
if(right[-1] < left[-1]):
    mxcat = left[-1]
    mxdir = "L"
    left.pop()
else:
    mxcat = right[-1]
    mxdir = "R"
    right.pop()

ans = 0

for i in range(n):
    #biggest cat can place
    if(place[i] != mxdir):
        continue

    temp = [0] * n
    temp[i] = mxcat #place biggest cat

    #place can't see cats first
    ridx = 0
    for j in range(i):
        if(place[j] == 'R'):
            temp[j] = right[ridx]
            ridx += 1

    lidx = 0
    for j in range(n-1, i, -1):
        if(place[j] == "L"):
            temp[j] = left[lidx]
            lidx += 1

    cnt = 1 #biggest cat
    leftmax = 0
    for j in range(i):
        if(place[j] == "L"):
            while lidx < len(left) and left[lidx] <= leftmax:
                lidx += 1
            if(lidx < len(left)):
                temp[j] = left[lidx]
                cnt += 1
        leftmax = max(leftmax, temp[j])

    rightmax = 0
    for j in range(n-1, i, -1):
        if(place[j] == "R"):
            while ridx < len(right) and right[ridx] <= rightmax:
                ridx += 1
            if(ridx < len(right)):
                temp[j] = right[ridx]
                cnt += 1
        rightmax = max(rightmax, temp[j])

    ans = max(ans, cnt)
    
print(ans)
