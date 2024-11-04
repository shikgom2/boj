import sys
input = sys.stdin.readline
import itertools

n = int(input())

li = []
for _ in range(n):
    a = list(map(str, input().rsplit()))
    li.append((a[0], float(a[1]), float(a[2])))
    
ans = 10**10
ans_li = []

li.sort(key=lambda x: x[2])
for i in range(n):
    tmp = 0
    tmp_li = []
    if(i >= 4):
        tmp = li[i][1] + li[0][2] + li[1][2] + li[2][2]
        tmp_li.append(li[i][0])
        tmp_li.append(li[0][0])
        tmp_li.append(li[1][0])
        tmp_li.append(li[2][0])
        
    else:
        for j in range(4):
            if(i == j):
                continue
            else:
                tmp += li[j][2]
                tmp_li.append(li[j][0])
        tmp += li[i][1]
        tmp_li.insert(0, li[i][0])
    
    if(ans > tmp):
        ans = tmp
        ans_li = []
        for i in range(len(tmp_li)):
            ans_li.append(tmp_li[i])

print(ans)
for i in range(4):
    print(ans_li[i])