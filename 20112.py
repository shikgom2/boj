import sys
input = sys.stdin.readline

n = int(input())
li = []
for _ in range(n):
    k = list(map(str, input().rstrip()))
    li.append(k)

ans1 = []
for i in range(n):
    for j in range(n):
        ans1.append(li[i][j])

ans2 = []
for i in range(n):
    for j in range(n):
        ans2.append(li[j][i])

flag = True
for i in range(len(ans1)):
    if(ans1[i] != ans2[i]):
        flag = False
if(flag):
    print("YES")
else:
    print("NO")