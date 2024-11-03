import sys
input = sys.stdin.readline
import itertools

n = int(input())

li = []
for _ in range(n):
    a = list(map(str, input().rsplit()))
    li.append((a[0], float(a[1]), float(a[2])))

li.sort(key=lambda x: x[2])

ans = 10**10
ans_idx = -1
ans_li = []
for i in range(len(li)):
    tmp = 0
    ans_li = []
    
    if(i >= 4):
        tmp += li[i][1] + li[0][2] + li[1][2] + li[2][2]
        ans_li = [li[i][0], li[0][0], li[0][1], li[2][0]]
    else:
        #0,1,2,3
        for j in range(5):
            if(i == j):
                tmp += li[j][1]
                ans_li.append(li[j][0])
            else:
                tmp += li[j][2]
                ans_li.append(li[j][0])
                
    if(ans > tmp):
        ans = tmp
        ans_idx = i

print(ans)
print(ans_li)