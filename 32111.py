import sys
input = sys.stdin.readline 

n = int(input())
li = list(map(str, input().rstrip()))

#1. So, if first index is O, it must be +.
#2. if continues X is even, it can't.
#3. else continuous X is odd, it can.


# 1. check if all characters are 'X'
if all(x == 'X' for x in li):
    print("YES")
    print("-" * n)
    exit()

# 2. check if all characters are 'O'
if all(x == 'O' for x in li):
    print("YES")
    print("+" * n)
    exit()

#find first O
first_o = 0
for i in range(len(li)):
    if(li[i] == 'O'):
        first_o = i
        break

li = li + li #circuler
flag = False
cnt = 0

for i in range(first_o, first_o + n):
    if li[i] == 'X':
        flag = True
        cnt += 1
    elif li[i] == 'O' and flag:
        flag = False
        if(cnt >= 2 and cnt % 2 == 0):  # It can't be resolved if an even-length segment of 'X's exists
            print("NO")
            exit()
        cnt = 0
if(cnt >= 2 and cnt % 2 == 0):
    print("NO")
    exit()

ans = []
i = first_o

while i < (first_o + n):
    if li[i] == 'O':
        ans.append("+")
        i += 1
    elif li[i] == 'X':
        count = 0
        # Count how many consecutive 'X'
        while i < (first_o + n) and li[i] == 'X':
            count += 1
            i += 1
        
        # Always count is odd (because of the previous check)
        for k in range(count // 2):
            ans.append("+")
        for k in range((count // 2) + 1):
            ans.append("-")
    else:
        i += 1

assert(len(ans) == n)

print("YES")
for i in range(first_o):
    print(ans[n-first_o+i], end="")

for i in range(n - first_o):
    print(ans[i], end="")