import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
tmp1 = 0
tmp2 = 0

for i in range(1, n+1):
    li = []

    for j in str(i):
        li.append(int(j))
    if len(li) == 1 or len(li) == 2:
        cnt += 1
    else:
        tmp1 = li[1] - li[0]
        tmp2 = li[2] - li[1]
        if tmp1 == tmp2:
            cnt += 1
print(cnt)
