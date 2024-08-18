import sys
input = sys.stdin.readline

n = int(input())
li = [[] for _ in range(5001)]

for _ in range(n):
    a,b= map(int, input().split())
    li[b].append(a)

ans = 0
for i in range(5001):

    l = len(li[i])
    li[i].sort()
    
    if(l > 0):
        for j in range(l):
            if(j == 0):
                ans = ans + abs(li[i][1]) - abs(li[i][0])
            elif(j == l-1):
                ans = ans + li[i][l-1] - li[i][l-2]
            else:
                ans = ans + min(abs(li[i][j] - li[i][j-1]), abs(li[i][j] - li[i][j+1]))
print(ans)