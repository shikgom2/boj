import sys
input = sys.stdin.readline

def check(li):
    ans = 0
    # check left
    max_height = 0
    for i in range(len(li)):
        if li[i][1] == 'R':
            max_height = max(max_height, li[i][0])
        else:
            if max_height < li[i][0]:
                max_height = li[i][0]
                ans += 1
                
    # check right
    max_height = 0
    for i in range(len(li) - 1, -1, -1):
        if li[i][1] == 'L':
            max_height = max(max_height, li[i][0])
        else:
            if max_height < li[i][0]:
                max_height = li[i][0]
                ans += 1
    return ans

n = int(input())

left = []
right = []
 
dp = [''] * n
for i in range(n):
    a, b = map(str, input().split())

    if(b == 'L'):
        dp[i] = 'L'
        left.append(int(a))
    else:
        dp[i] = 'R'
        right.append(int(a))

#case 1 left asc, right asc
left.sort()
right.sort()

li = []
cur_left = 0
cur_right = 0
for i in range(n):
    if(dp[i] == 'L'):
       li.append((left[cur_left], "L")) 
       cur_left += 1
    else:
        li.append((right[cur_right], "R"))
        cur_right += 1

ans1 = check(li)

#case 2 left desc, right asc
left.sort(reverse=True)
right.sort()

li = []
cur_left = 0
cur_right = 0
for i in range(n):
    if(dp[i] == 'L'):
       li.append((left[cur_left], "L")) 
       cur_left += 1
    else:
        li.append((right[cur_right], "R"))
        cur_right += 1
ans2 = check(li)

#case 3 left asc, right desc
left.sort()
right.sort(reverse=True)

li = []
cur_left = 0
cur_right = 0
for i in range(n):
    if(dp[i] == 'L'):
       li.append((left[cur_left], "L")) 
       cur_left += 1
    else:
        li.append((right[cur_right], "R"))
        cur_right += 1
ans3 = check(li)

#case 4
left.sort(reverse=True)
right.sort(reverse=True)

li = []
cur_left = 0
cur_right = 0
for i in range(n):
    if(dp[i] == 'L'):
       li.append((left[cur_left], "L")) 
       cur_left += 1
    else:
        li.append((right[cur_right], "R"))
        cur_right += 1
ans4 = check(li)

print(max(ans1, ans2, ans3, ans4))
