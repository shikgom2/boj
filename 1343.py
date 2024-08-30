import sys
input = sys.stdin.readline

li = list(map(str, input().rstrip()))

ans = []
cur = li[0]
count = 1

for i in range(1, len(li)):
    if li[i] == cur:
        count += 1
    else:
        ans.append((cur, count))
        cur = li[i]
        count = 1
ans.append((cur, count))

res = []
for i in range(len(ans)):
    if(ans[i][0] == 'X'):
        if(ans[i][1] %2 == 1):
            print(-1)
            exit()
        cnt1 = ans[i][1] // 4
        res.append('A' * (cnt1 * 4))
        if(ans[i][1] % 4 == 2):
            res.append('BB')
    else:
        res.append('.' * ans[i][1])

print(*res, sep="")