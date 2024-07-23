import sys
input = sys.stdin.readline

n = int(input())
li = list(map(str, input().rstrip()))

ans = []
str1 = ''

for i in range(int(len(li) / n)):
    if i % 2 == 1:
        str1 = li[i*n:i*n+n]
        ans.append(str1[::-1])
    else:
        ans.append(li[i*n:i*n+n])

for i in range(n):
    for j in range(int(len(li)/ n)):
        print(ans[j][i], end="")
