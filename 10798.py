import sys
input = sys.stdin.readline

li = [[""] * 15 for _ in range(15)]

for i in range(5):
    s = list(map(str, input().rstrip()))
    for j in range(len(s)):
        li[i][j] = s[j]

ans = []
for i in range(15):
    for j in range(5):
        if(li[j][i] != ""):
            ans.append(li[j][i])
print(*ans,sep="")