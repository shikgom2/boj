import sys
input = sys.stdin.readline

N = int(input())
arr = input().split()

li = []
for a in arr:
    tmp = int(a)
    if(tmp == 0):
        tmp = "000000000000000"
    else:
        while tmp <= 10**13:
            tmp *= 10

    li.append((a, str(tmp)))

li.sort(key=lambda k: k[1], reverse=True)
ans = []
for a in li:
    ans.append(a[0])

ans = ''.join(ans).lstrip('0')
if(ans == ""):
    print(0)
else:
    print(ans)
